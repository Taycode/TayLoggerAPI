from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status
from .serializers import LogGroupSerializer


class CreateLogGroup(APIView):

    serializer_class = LogGroupSerializer

    @staticmethod
    def post(request):
        serializer = LogGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
