from rest_framework.serializers import ModelSerializer
from .models import LogGroup, Log


class LogGroupSerializer(ModelSerializer):

    class Meta:
        model = LogGroup
        fields = "__all__"

class LogSerializer(ModelSerializer):

    class Meta:
        model = Log
        fields = "__all__"
