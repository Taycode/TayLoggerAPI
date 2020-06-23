from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import LogGroupSerializer, LogSerializer


class CreateLogGroup(APIView):

    serializer_class = LogGroupSerializer
    permission_classes = (IsAuthenticated, )

    @staticmethod
    def post(request):
        serializer = LogGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateLog(APIView):

    serializer_class = LogSerializer
    permission_classes = (IsAuthenticated, )

    @staticmethod
    def post(request):
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
