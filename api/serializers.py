from rest_framework import serializers
from .models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'task_title', 'task_content', 'task_data',
                  'task_hour', 'task_completed', 'task_remember',
                  'task_created')


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('task_title', 'task_content', 'task_data',
                  'task_hour', 'task_remember')
