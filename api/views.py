from rest_framework import status
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from drf_yasg.utils import swagger_auto_schema, no_body
from .models import Photo, Like
from .serializers import (
    UserSerializer,
    PhotoSerializer,
    LikeSerializer,
    CommentSerializer
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
    queryset = Photo.objects.none()
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=no_body,
        responses={'200': PhotoSerializer()},
        operation_description="Approve a photo")
    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def approve(self, request, pk=None):
        photo = self.get_object()
        photo.status = 1
        photo.save()
        serializer = self.get_serializer(photo)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=no_body,
        responses={'200': PhotoSerializer()},
        operation_description="Decline a photo")
    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def decline(self, request, pk=None):
        photo = self.get_object()
        photo.status = 2
        photo.save()
        serializer = self.get_serializer(photo)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=no_body,
        tags=['likes'],
        method='post',
        responses={'200': LikeSerializer()},
        operation_description="Like a photo")
    @swagger_auto_schema(
        request_body=no_body,
        tags=['likes'],
        method='get',
        responses={'200': LikeSerializer()},
        operation_description="Get likes")
    @action(detail=True, methods=['get', 'post'])
    def like(self, request, pk=None):
        match request.method:
            case 'GET':
                photo = self.get_object()
                queryset = photo.likes.all()
                serializer = LikeSerializer(queryset, many=True)
                return Response(serializer.data)
            case 'POST':
                photo = self.get_object()
                user = self.request.user
                like = Like.objects.get_or_create(photo=photo, user=user)
                like = like[0]
                like.save()
                return Response({"user": user.id, "photo": photo.id})

    @swagger_auto_schema(
        request_body=CommentSerializer,
        tags=['comments'],
        method='post',
        responses={'200': CommentSerializer()},
        operation_description="Comment in a photo")
    @swagger_auto_schema(
        tags=['comments'],
        method='get',
        responses={'200': CommentSerializer()},
        operation_description="Get comments")
    @action(detail=True, methods=['get', 'post'])
    def comment(self, request, pk=None):
        match request.method:
            case 'GET':
                photo = self.get_object()
                queryset = photo.comments.all()
                serializer = CommentSerializer(queryset, many=True)
                return Response(serializer.data)
            case 'POST':
                photo = self.get_object()
                author = self.request.user
                serializer = CommentSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save(author=author, photo=photo)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Photo.objects.all()
        return Photo.objects.filter(status=1)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
