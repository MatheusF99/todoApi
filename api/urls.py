from django.urls import path
from rest_framework import views
from .views import TaskView, CreateTaskView, GetTask, DeleteTaskView, welcome

urlpatterns = [
    # UserUrls
    # tasks urls
    path('tasks', TaskView.as_view()),
    path('create', CreateTaskView.as_view()),
    path('list', GetTask.as_view()),
    path('deleted/<uuid:task_id>',  DeleteTaskView.as_view()),
    path('welcome', welcome)
]
