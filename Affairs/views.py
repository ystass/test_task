from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (CreateAPIView, UpdateAPIView,
                                     DestroyAPIView, RetrieveAPIView, ListAPIView)

from Affairs.models import Tasks
from Affairs.pagination import TasksPaginator
from Affairs.serializer import TasksSerializer


class TasksCreateAPIView(CreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


class TasksUpdateAPIView(UpdateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


class TasksDestroyAPIView(DestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


class TasksRetrieveAPIView(RetrieveAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


class TasksListAPIView(ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    pagination_class = TasksPaginator
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = (
        "tags",
        "is_completed",
    )
    ordering_fields = ("due_date", "created_at", "title")
