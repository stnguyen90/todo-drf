from django.contrib.auth.models import User, Group
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from tododrf.api.models import TaskList, Task


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class OwnerFilteredPrimaryKeyRelatedField(PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super().get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(owner=request.user)


class TaskListSerializer(ModelSerializer):
    parent = OwnerFilteredPrimaryKeyRelatedField(
        queryset=TaskList.objects, allow_null=True)

    class Meta:
        model = TaskList
        fields = '__all__'
        read_only_fields = ['owner']


class TaskSerializer(ModelSerializer):
    task_list = OwnerFilteredPrimaryKeyRelatedField(queryset=TaskList.objects)
    parent = OwnerFilteredPrimaryKeyRelatedField(
        queryset=Task.objects, allow_null=True)

    class Meta:
        model = Task
        fields = '__all__'
