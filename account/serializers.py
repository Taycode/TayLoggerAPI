from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from django.contrib.auth import authenticate
from .models import User



class CreateUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True}
        }

    @staticmethod
    def validate_email(email):
        if User.objects.filter(email__iexact=email):
            raise ValidationError("Email Already Exists")
        return email


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def authenticate_user(self):
        if self.is_valid():
            if not User.objects.filter(email__iexact=self.validated_data["email"]):
                return Response({"message": "Wrong Credentials"}, status=HTTP_400_BAD_REQUEST)

            username = User.objects.get(email__iexact=self.validated_data["email"]).username
            user = authenticate(username=username, password=self.validated_data["password"])
            if user is not None:
                return Response({"token": user.auth_token.key}, status=HTTP_200_OK)
            else:
                return Response({"message": "Wrong Credentials"}, status=HTTP_400_BAD_REQUEST)

        else:
            return Response(self.errors, status=HTTP_400_BAD_REQUEST)
