from django.urls import path
from Affairs.apps import AffairsConfig

from Affairs.views import (TasksCreateAPIView, TasksUpdateAPIView,
                           TasksDestroyAPIView, TasksRetrieveAPIView,
                           TasksListAPIView)

app_name = AffairsConfig.name

urlpatterns = [
    path(
        "tasks/create/", TasksCreateAPIView.as_view(), name="create-tasks"
    ),
    path(
        "tasks/<int:pk>/update/", TasksUpdateAPIView.as_view(), name="update-tasks"
    ),
    path(
        "tasks/<int:pk>/delete/", TasksDestroyAPIView.as_view(), name="delete-tasks"
    ),
    path(
        "tasks/<int:pk>/", TasksRetrieveAPIView.as_view(), name="retrieve-tasks"
    ),
    path(
        "tasks/", TasksListAPIView.as_view(), name="list-tasks"
    ),
]
