from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to check if user is owner.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsTaskListOwner(permissions.BasePermission):
    """
    Custom permission to check if user is owner.
    """

    def has_object_permission(self, request, view, obj):
        return obj.task_list.owner == request.user
