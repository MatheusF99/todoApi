# Generated by Django 3.2 on 2021-05-07 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user_name', models.CharField(max_length=100, unique=True)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_passworld', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('task_created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('task_title', models.CharField(max_length=255)),
                ('task_content', models.CharField(max_length=255)),
                ('task_data', models.CharField(max_length=10)),
                ('task_hour', models.CharField(max_length=5)),
                ('task_completed', models.BooleanField(default=False)),
                ('task_remember', models.BooleanField(default=False)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
    ]
