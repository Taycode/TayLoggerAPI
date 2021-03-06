from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CreateUserSerializer, LoginSerializer


class UserCreateView(APIView):

    serializer_class = CreateUserSerializer

    @staticmethod
    def post(request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    serializer_class = LoginSerializer

    @staticmethod
    def post(request):
        serializer = LoginSerializer(data=request.data)
        return serializer.authenticate_user()
