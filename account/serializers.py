from rest_framework.serializers import ModelSerializer, ValidationError
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
