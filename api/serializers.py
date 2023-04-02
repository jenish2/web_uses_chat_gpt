from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import ListField

from api.models import UserProject, Suggestion,UserFolder


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = "__all__"


def create_suggestions(suggestion_list, user_project_id):
    for suggestion in suggestion_list:
        data = {
            "suggestion": suggestion,
            "user_project_id": user_project_id
        }
        serialize = SuggestionSerializer(data=data)
        if serialize.is_valid():
            serialize.save()


class ProjectSerializer(serializers.ModelSerializer):
    suggestions_list = ListField(child=serializers.CharField(max_length=255))

    class Meta:
        model = UserProject
        fields = (
            'user_email', 'project_name', 'project_slug', 'category_slug', 'project_text', 'suggestions_list','user_folder_id')

    def validate(self, data):
        project_text = data.get('project_text', None)

        if project_text is None:
            raise ValidationError("Validated project text")
        return data

    def create(self, validated_data):
        suggestion_list = validated_data.pop('suggestions_list')
        user_project = UserProject.objects.create(**validated_data)
        user_project_id = user_project.id
        create_suggestions(suggestion_list, user_project_id)
        return user_project


class GetProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProject
        fields = "__all__"

class UserFolderSerializer(serializers.ModelSerializer):
    child_folders = serializers.SerializerMethodField()
    
    class Meta:
        model = UserFolder
        fields = ["id","user_email","folder_name","parent_folder","child_folders"]

    def get_child_folders(self, obj):
        serializer = self.__class__(obj.child_folders.all(), many=True)
        return serializer.data
