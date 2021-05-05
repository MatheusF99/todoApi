import json
from django.shortcuts import render
from .serializers import TaskSerializer, CreateTaskSerializer
from .models import Tasks
from rest_framework import generics, serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class TaskView(APIView):
    querySet = Tasks.objects.all()
    serializer_class = TaskSerializer


class GetTask(APIView):
    serializer_class = TaskSerializer

    def get(self, request, format=json):
        tasks = Tasks.objects.all()
        data = []
        for i in range(0, len(tasks)):
            data.append(TaskSerializer(tasks[i]).data)
        return Response(data, status=status.HTTP_200_OK)


class CreateTaskView(APIView):
    serializer_class = CreateTaskSerializer

    def post(self, request, format=None):
        # if not self.request.session.exists(self.request.session.session_key):
        #     self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        print(serializer)

        task_content = request.data.get('task_content')
        task_data = request.data.get('task_data')
        task_hour = request.data.get('task_hour')
        task_remember = request.data.get('task_remember')
        # print(self.request.session.session_key)

        #querySet = Tasks.objects.all()
        print(task_content)
        tasks = Tasks(task_content=task_content, task_data=task_data,
                      task_hour=task_hour, task_remember=task_remember)

        tasks.save()

        return Response(TaskSerializer(tasks).data, status=status.HTTP_200_OK)
