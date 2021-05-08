from django.db import models
import uuid
from datetime import datetime

from django.db.models.deletion import CASCADE
from django.conf import settings
from django.utils import timezone

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class User(models.Model):
    user_id = models.UUIDField(
        null=False,
        unique=True,
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user_name = models.CharField(max_length=100, null=False, unique=True)
    user_email = models.EmailField(max_length=254, unique=True, null=False)
    user_passworld = models.CharField(max_length=255, null=False)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True)

    def __str__(self):
        return self.user_name

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


class Tasks(models.Model):
    id = models.UUIDField(
        null=False,
        unique=True,
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    task_created = models.DateTimeField(default=timezone.now, blank=True)
    task_title = models.CharField(max_length=255, null=False)
    task_content = models.CharField(max_length=255, null=False)
    task_data = models.CharField(max_length=10, null=False)
    task_hour = models.CharField(null=False, max_length=5)
    task_completed = models.BooleanField(default=False)
    task_remember = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __repr__(self):
        return "<Task %s>" % self.id
