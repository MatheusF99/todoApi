from django.db.models import fields
from rest_framework import serializers
from .models import Tasks, User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name', 'user_email', 'user_passworld']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
            'id',
            'task_title',
            'task_content',
            'task_data',
            'task_hour',
            'task_completed',
            'task_remember',
            'task_created'
        ]


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = (
            'task_title',
            'task_content',
            'task_data',
            'task_hour',
            'task_remember'
        )


class DeleteTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id')
