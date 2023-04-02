from django.db import models

class DB_CONFIG:
    HOME_DIR_NAME = "Home" # name of home directory


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserFolder(BaseModel):
    user_email = models.EmailField(max_length=255)
    folder_name = models.CharField(max_length=255)
    parent_folder = models.ForeignKey('self',on_delete=models.CASCADE,null=True,
                                      blank=True, related_name='child_folders')

class UserData(models.Model):
    user_email = models.EmailField(max_length=255)
    number_of_words = models.IntegerField(default=0)

class UserProject(BaseModel):
    user_email = models.EmailField(max_length=255)
    project_name = models.CharField(max_length=255)
    project_slug = models.CharField(max_length=255)
    category_slug = models.CharField(max_length=255)
    project_text = models.TextField(max_length=255)
    user_folder = models.ForeignKey(UserFolder, on_delete=models.CASCADE)

class Suggestion(BaseModel):
    user_project_id = models.ForeignKey(UserProject, on_delete=models.CASCADE)
    suggestion = models.CharField(max_length=255)
