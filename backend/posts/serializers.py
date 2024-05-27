from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
from likes.serializers import LikeSerializer
from comments.serializers import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'user_id', 'title', 'content', 'created_at', 'updated_at', 'likes', 'likes_count', 'comments', 'comments_count']
        