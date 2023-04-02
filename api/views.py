from decouple import config
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from chat_gpt.chat_gpt import ChatGpt
from .DTO.UserProjectDTO import UserProjectDTO
from .models import UserProject, Suggestion, UserFolder, DB_CONFIG, UserData
from .project_config import PROJECT_CATEGORIES
from .serializers import ProjectSerializer, SuggestionSerializer, GetProjectSerializer, create_suggestions, \
    UserFolderSerializer

# utility class for views
class ViewsUtils(object):
    # get home folder of user
    def get_home_folder(self, email):
        home_dir = UserFolder.objects.filter(user_email=email, parent_folder__isnull=True,
                                             folder_name=DB_CONFIG.HOME_DIR_NAME)
        return home_dir[0] if len(home_dir) > 0 else False

    # create home folder if not present
    def create_home_directory_if_not_present(self, email):
        home_dir = self.get_home_folder(email)

        if not home_dir:
            UserFolder(
                user_email=email,
                folder_name=DB_CONFIG.HOME_DIR_NAME,
            ).save()

    # get number of tokens(words) user has used
    def get_number_of_words(self, email):
        data = UserData.objects.filter(user_email=email)
        if data.count() > 0:
            n_words = data.first().number_of_words
            return n_words, data.first()
        else:
            user_data = UserData(user_email=email, number_of_words=0).save()
            return 0, user_data

    # increase number of tokens(words) user has used
    def increase_number_of_words(self, email, count):
        n_words, obj = self.get_number_of_words(email)
        obj.number_of_words = n_words + count
        obj.save()


# Suggenstion view
class SuggestionList(APIView):
    """returns ai generated suggestions"""
    view_utils = ViewsUtils()
    permission_classes = [IsAuthenticated]

    # get list of suggestions for a project
    def post(self, request):
        data = request.data
        my_model = ChatGpt(config("CHAT_GPT_API_KEY"))

        input_data = data.get("data")
        project_slug = data.get("project_slug")
        category_slug = data.get("category_slug")
        number_of_responses = data.get("number_of_responses", 1)

        query = self.__get_query(input_data, project_slug, category_slug)

        response_list_from_chat_gpt, total_tokens = my_model.get_suggestions(query, number_of_responses)

        self.view_utils.increase_number_of_words(request.user.email, total_tokens)

        return Response(
            {
                "descriptions": response_list_from_chat_gpt,
                "status": "success",
            },
            status=status.HTTP_200_OK,
        )

    # get gpt3 query for given project
    def __get_query(self, input_data, project_slug, category_slug):
        query = ""
        project_config = PROJECT_CATEGORIES[category_slug][project_slug]
        if project_config:
            query = project_config["query_string"]
            fields = project_config["fields"]

            query_data = {}
            for field in fields:
                field_key = field["name"]
                query_data[field_key] = input_data.get(field_key, field["default_value"])

            query = query.format(**query_data).replace("\n", "")
        return query

# save project in the database
class SaveProject(viewsets.ViewSet):
    "To save and Update a project"
    permission_classes = [IsAuthenticated]

    view_utils = ViewsUtils()

    # save project text & name
    def save_project(self, request):
        try:
            data = request.data
            user_email = request.user.email

            # save project in root folder
            self.view_utils.create_home_directory_if_not_present(user_email)
            user_folder_id = self.view_utils.get_home_folder(user_email).id

            UserProject(user_email=user_email, project_name=data['project_name'], user_folder_id=user_folder_id,
                        project_text=data['project_text'], category_slug=data['category_slug'],
                        project_slug=data['project_slug']).save()

            return Response("Project Saved Successfully", status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response("IN VALID DATA", status=status.HTTP_400_BAD_REQUEST)

    
    def get_project_list_by_folder(self,request):
        user_email = request.user.email
        folder_id = request.data.get('folder_id')
        if not folder_id:
            folder_id = self.view_utils.get_home_folder(user_email).id

        user_project_query = UserProject.objects.filter(user_email=user_email,user_folder_id=folder_id)
        user_project_data_list = GetProjectSerializer(user_project_query, many=True).data

        user_project_dto_list = []

        for project in user_project_data_list:
            
            user_project_dto_list.append(
                UserProjectDTO(dict(project)).user_project_without(user_email=True, project_text=True,
                                                                   suggestion_list=True))

        return Response(data=user_project_dto_list)

    # return project details by project id
    def get_project_details_by_id(self, request):
        project_id = request.data.get('project_id')

        user_project_query = UserProject.objects.filter(id=project_id)
        user_project_data = GetProjectSerializer(user_project_query, many=True).data

        if not user_project_data:
            return Response("Project ID Does Not Exist", status=status.HTTP_404_NOT_FOUND)

        user_project_data = dict(user_project_data[0])

        suggetions_query = Suggestion.objects.filter(user_project_id=project_id)
        suggetions = SuggestionSerializer(suggetions_query, many=True).data

        user_project_data["suggestions_list"] = suggetions

        return Response(data=UserProjectDTO(dict(user_project_data)).user_project_dto())

    # update project details
    def update_project(self, request):
        try:
            data = request.data
            project_id = data.get('id')
            project_name = data.get('project_name')
            project_text = data.get('project_text')
            suggestion_list = data.get('suggestions_list')

            user_project = UserProject.objects.get(id=project_id)
            user_project.project_name = project_name
            user_project.project_text = project_text
            user_project.save()

            suggestions = Suggestion.objects.filter(user_project_id=project_id)

            suggestions.delete()

            create_suggestions(suggestion_list, project_id)
        except:
            return Response("Failed to update project")

        return Response("Updated project")

    # delete project by id
    def delete_project(self, request):
        project_id = request.data.get('project_id')
        try:
            user_project = UserProject.objects.get(id=project_id)
            user_project.delete()
        except:
            return Response("Project Does Not Exist")
        return Response(f"Deleted project with id {project_id}")


# View for creating, listing and deleting folders 
class UserFolders(viewsets.ViewSet):
    "To save and Update a project"
    permission_classes = [IsAuthenticated]

    view_utils = ViewsUtils()

    # create new folder
    def create(self, request):
        user_email = request.user.email
        try:
            data = request.data
            folder_name = data.get("folder_name")

            self.view_utils.create_home_directory_if_not_present(user_email)
            homedir = self.view_utils.get_home_folder(user_email)

            if homedir:
                UserFolder(
                    user_email=user_email,
                    folder_name=folder_name,
                    parent_folder=homedir
                ).save()
                return Response(f"Folder Created Successfully ", status=status.HTTP_201_CREATED)

            return Response("InValid Data", status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("InValid Data", status=status.HTTP_400_BAD_REQUEST)

    # list all the folders
    def list_all(self, request):
        user_email = request.user.email
        self.view_utils.create_home_directory_if_not_present(user_email)

        my_folder = UserFolderSerializer(self.view_utils.get_home_folder(user_email)).data
        return Response(data=my_folder)

    # delete folder by id
    def delete_by_id(self, request):
        user_email = request.user.email
        try:
            data = request.data
            id = data.get("id")
            UserFolder.objects.filter(id=id, user_email=user_email).delete()
            return Response("Deleted Successfully", status=status.HTTP_200_OK)
        except:
            return Response("InValid Data", status=status.HTTP_400_BAD_REQUEST)
        
    # add project to folder
    def put_project_in_folder(self,request):
        user_email = request.user.email
        try:
            data = request.data
            project_id = data.get("project_id")
            folder_id = data.get("folder_id")

            project = UserProject.objects.get(id=project_id)
            project.user_folder = UserFolder.objects.get(id=folder_id)
            project.save()
            return Response("File Added Successfully", status=status.HTTP_200_OK)
        except:
            return Response("InValid Data", status=status.HTTP_400_BAD_REQUEST)

    def rename_folder(self,request):
        user_email = request.user.email
        try:
            data = request.data
            folder_id = data.get("folder_id")
            folder_name = data.get("folder_name")

            folder = UserFolder.objects.get(id=folder_id)
            folder.folder_name = folder_name
            folder.save()
            return Response("Folder Renamed Successfully", status=status.HTTP_200_OK)
        except:
            return Response("InValid Data", status=status.HTTP_400_BAD_REQUEST)

# View for handling words/tokens
class UserWords(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    view_utils = ViewsUtils()

    # returns number of tokens user has used
    def get_number_of_words(self, request):
        user_email = request.user.email
        return Response({
            "n_words": self.view_utils.get_number_of_words(user_email)[0],
        })
