import json
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import TaskSerializer, CreateTaskSerializer, DeleteTaskSerializer
from .models import Tasks
from rest_framework import generics, serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response

# autenticacao
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def welcome(request):
    content = {'message': 'Bem-vindo a todolist'}
    return JsonResponse(content)


class TaskView(APIView):
    querySet = Tasks.objects.all()
    serializer_class = TaskSerializer


class GetTask(APIView):
    def get(self, request, format=json):
        tasks = Tasks.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse({'tasks': serializer.data}, safe=False, status=status.HTTP_200_OK)


class CreateTaskView(APIView):
    serializer_class = CreateTaskSerializer

    def post(self, request, format=None):
        # if not self.request.session.exists(self.request.session.session_key):
        #     self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        print(serializer)

        task_title = request.data.get('task_title')
        task_content = request.data.get('task_content')
        task_data = request.data.get('task_data')
        task_hour = request.data.get('task_hour')
        task_remember = request.data.get('task_remember')
        # print(self.request.session.session_key)

        #querySet = Tasks.objects.all()
        print(task_content)
        tasks = Tasks(
            task_title=task_title,
            task_content=task_content,
            task_data=task_data,
            task_hour=task_hour,
            task_remember=task_remember
        )

        tasks.save()

        return Response(TaskSerializer(tasks).data, status=status.HTTP_200_OK)


class DeleteTaskView(APIView):
    serializer_class = DeleteTaskSerializer

    def delete(self, request, task_id, format=None):
        task_selected = Tasks.objects.get(id=task_id)
        try:
            task_selected.delete()
            return Response({'message': 'deleted'}, status=status.HTTP_200_OK)
        except Tasks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
