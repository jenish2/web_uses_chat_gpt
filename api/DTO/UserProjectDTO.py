from api.DTO.SuggestionDTO import SuggestionDTO


class UserProjectDTO:

    def __init__(self, user_project_dict):
        self.suggestions_list = []
        self.id = user_project_dict.get('id')
        self.user_email = user_project_dict.get('user_email')
        self.project_name = user_project_dict.get('project_name')
        self.project_slug = user_project_dict.get('project_slug')
        self.category_slug = user_project_dict.get('category_slug')
        self.project_text = user_project_dict.get('project_text')
        self.updated_at = user_project_dict.get('updated_at')

        if user_project_dict.get('suggestions_list'):
            for suggestion in user_project_dict.get('suggestions_list'):
                suggest = suggestion
                x = type(suggestion)
                if type(suggestion) is str:
                    dic = dict()
                    dic['suggestion'] = suggestion
                    dic['user_project_id'] = 0
                    suggest = dic
                self.suggestions_list.append(SuggestionDTO(suggest).get_suggestion_without_project_id())

    def give_basic_dict(self):
        return self.__dict__

    def user_project_dto(self):
        return self.give_basic_dict()

    def user_project_without(self, user_email=False, project_name=False, project_slug=False, category_slug=False,
                             project_text=False, suggestion_list=False):
        user_project = self.give_basic_dict()
        if project_name:
            user_project.pop('project_name')
        if user_email:
            user_project.pop('user_email')
        if project_slug:
            user_project.pop('project_slug')
        if category_slug:
            user_project.pop('category_slug')
        if project_text:
            user_project.pop('project_text')
        if suggestion_list:
            user_project.pop('suggestions_list')
        return user_project
