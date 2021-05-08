from django.urls import path
from rest_framework import views
from .views import CreateTaskView, GetTask, DeleteTaskView, welcome, CreateUserView

urlpatterns = [
    # UserUrls
    path('create_user', CreateUserView),
    # tasks urls
    path('create', CreateTaskView),
    path('list', GetTask),
    path('deleted/<uuid:task_id>',  DeleteTaskView.as_view()),
    path('welcome', welcome)
]
