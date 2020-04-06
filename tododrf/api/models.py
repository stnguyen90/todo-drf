from django.contrib.auth.models import User
from django.db import models


class TaskList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Task(models.Model):
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    summary = models.CharField(max_length=50)
    notes = models.CharField(max_length=200)
