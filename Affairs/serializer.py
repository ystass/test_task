from rest_framework.serializers import ModelSerializer

from Affairs.models import Tasks


class TasksSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"
