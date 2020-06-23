from rest_framework.serializers import ModelSerializer
from .models import LogGroup, Log


class LogGroupSerializer(ModelSerializer):

    class Meta:
        model = LogGroup
        fields = "__all__"
        extra_kwargs = {
            "user": {
                "required": False
            }
        }


class LogSerializer(ModelSerializer):

    class Meta:
        model = Log
        fields = "__all__"
