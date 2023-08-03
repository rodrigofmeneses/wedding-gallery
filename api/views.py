from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import (
    UserSerializer,
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


# class CreatePhotoView(APIView):
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(author=request.user) 
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CreateCommentView(APIView):
#     def post(self, request, post_id):
#         post = Photo.objects.get(id=post_id)
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(post=post, author=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class AddLikeView(APIView):
#     def post(self, request, post_id):
#         post = Photo.objects.get(id=post_id)
#         serializer = LikeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(post=post, user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
