from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
from likes.serializers import LikeSerializer

class PostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'user_id', 'title', 'content', 'created_at', 'updated_at', 'likes']
        