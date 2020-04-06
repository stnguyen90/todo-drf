from rest_framework import routers

from tododrf.api import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'task_lists', views.TaskListViewSet)
router.register(r'tasks', views.TaskViewSet)

urlpatterns = router.urls
