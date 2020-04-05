from django.contrib.auth.models import User, Group
from rest_framework import serializers

from tododrf.api.models import TaskList, Task


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class TaskListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskList
        fields = ['url', 'parent', 'name']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['url', 'parent', 'summary', 'notes']
