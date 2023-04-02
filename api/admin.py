from django.contrib import admin

from api.models import UserProject, Suggestion

# Register your models here.
admin.site.register(UserProject)
admin.site.register(Suggestion)