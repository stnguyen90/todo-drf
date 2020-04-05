from django.db import models


class TaskList(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Task(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    summary = models.CharField(max_length=50)
    notes = models.CharField(max_length=200)
