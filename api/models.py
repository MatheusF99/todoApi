from django.db import models
import uuid
from datetime import datetime

from django.db.models.deletion import CASCADE

# Create your models here.


# class User(models.Model):
#     user_id = models.UUIDField(
#         null=False,
#         unique=True,
#         primary_key=True,
#         default=uuid.uuid4,
#         editable=False
#     )
#     user_name = models.CharField(max_length=100, null=False, unique=True)
#     user_email = models.EmailField(max_length=254, unique=True, null=False)
#     user_passworld = models.CharField(max_length=255, null=False)
#     created_date = models.DateTimeField(default=datetime.utcnow)

#     def __str__(self):
#         return self.user_name


class Tasks(models.Model):
    id = models.UUIDField(
        null=False,
        unique=True,
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    #user = models.ForeignKey(User, on_delete=CASCADE)
    task_created = models.DateTimeField(auto_now_add=True, blank=True)
    task_title = models.CharField(max_length=255, null=False)
    task_content = models.CharField(max_length=255, null=False)
    task_data = models.CharField(max_length=10, null=False)
    task_hour = models.CharField(null=False, max_length=5)
    task_completed = models.BooleanField(default=False)
    task_remember = models.BooleanField(default=False)

    def __repr__(self):
        return "<Task %s>" % self.id
