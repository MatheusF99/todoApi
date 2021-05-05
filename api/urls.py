from django.urls import path
from .views import TaskView, CreateTaskView, GetTask

urlpatterns = [
    path('tasks', TaskView.as_view()),
    path('create', CreateTaskView.as_view()),
    path('list', GetTask.as_view())
]
