from django.contrib import admin

from tododrf.api.models import TaskList, Task

admin.site.register(TaskList)
admin.site.register(Task)
