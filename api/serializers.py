from rest_framework import serializers
from .models import User, Photo, Comment, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class PhotoSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Photo
        fields = ['id', 'author', 'url', 'status', 'created_at']
        read_only_fields = ['author', 'status', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'photo', 'author', 'content', 'created_at']
        read_only_fields = ['photo', 'author', 'created_at']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'photo', 'user', 'created_at']
        read_only_fields = ['photo', 'user', 'created_at']
