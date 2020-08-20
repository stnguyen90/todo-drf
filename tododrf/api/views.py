from django.contrib.auth.models import User, Group
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework import permissions

from tododrf.api.models import TaskList, Task
from tododrf.api.serializers import (
    TaskListSerializer,
    TaskSerializer,
    UserSerializer,
    GroupSerializer
)
from tododrf.api.permissions import IsOwner, IsTaskListOwner


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    filterset_fields = UserSerializer.Meta.fields


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]
    filterset_fields = GroupSerializer.Meta.fields


class TaskListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows task lists to be viewed or edited.
    """
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filterset_fields = TaskListSerializer.Meta.fields

    def perform_create(self, serializer):
        """
        Hook into create and set owner as authenticated user.
        """
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        This view should return a list of all the task lists
        for the currently authenticated user.
        """
        user = self.request.user
        return TaskList.objects.filter(owner=user)


def task_lists(request):
    if request is None:
        return TaskList.objects.none()

    return TaskList.objects.filter(owner=request.user)


class TaskFilter(filters.FilterSet):
    task_list = filters.ModelChoiceFilter(queryset=task_lists)

    class Meta:
        model = Task
        fields = TaskSerializer.Meta.fields


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsTaskListOwner]
    filterset_class = TaskFilter

    def get_queryset(self):
        """
        This view should return a list of all the task lists
        for the currently authenticated user.
        """
        user = self.request.user
        task_lists = TaskList.objects.filter(owner=user)
        return Task.objects.filter(task_list__in=task_lists)
