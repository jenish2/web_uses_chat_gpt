from django.urls import path

from .views import SuggestionList, SaveProject,UserFolders,UserWords

urlpatterns = [
    path('get_suggestions', SuggestionList.as_view()),
    path('save_project', SaveProject.as_view({'post': 'save_project'})),
    path('get_project_list_by_folder', SaveProject.as_view({'post': 'get_project_list_by_folder'})),
    path('get_project_details_by_id', SaveProject.as_view({'post': 'get_project_details_by_id'})),
    path('update_project_details', SaveProject.as_view({'post': 'update_project'})),
    path('delete_project', SaveProject.as_view({'post': 'delete_project'})),
    path('create_folder', UserFolders.as_view({'post': 'create'})),
    path('list_folders', UserFolders.as_view({'post': 'list_all'})),
    path('delete_folder', UserFolders.as_view({'post': 'delete_by_id'})),
    path('rename_folder', UserFolders.as_view({'post': 'rename_folder'})),
    path('number_of_words', UserWords.as_view({'post': 'get_number_of_words'})),
    path('put_project_in_folder', UserFolders.as_view({'post': 'put_project_in_folder'})),
]
