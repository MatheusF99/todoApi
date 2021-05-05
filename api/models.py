from django.db import models
import uuid
from datetime import datetime

# Create your models here.


class Tasks(models.Model):
    id = models.UUIDField(null=False, unique=True,
                          primary_key=True, default=uuid.uuid4, editable=False)
    task_created = models.DateTimeField(auto_now_add=True, blank=True)
    task_content = models.CharField(max_length=255, null=False)
    task_data = models.CharField(max_length=10, null=False)
    task_hour = models.CharField(null=False, max_length=5)
    task_completed = models.BooleanField(default=False)
    task_remember = models.BooleanField(default=False)

    def __repr__(self):
        return "<Task %s>" % self.id
