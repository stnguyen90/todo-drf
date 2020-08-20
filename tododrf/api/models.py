from django.contrib.auth.models import User
from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TaskList(TimeStampMixin):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(TimeStampMixin):
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    summary = models.CharField(max_length=50)
    notes = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.summary
