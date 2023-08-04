from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import Photo
from .serializers import (
    UserSerializer,
    PhotoSerializer
)


class RegisterUserView(APIView):
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={'201': UserSerializer()},
        operation_description="Register user on system")
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhotosViewset(ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.filter(status=1)

