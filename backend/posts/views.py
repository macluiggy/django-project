from django.shortcuts import render
from requests import Request
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from comments.models import Comment
from likes.models import Like
from .serializers import PostSerializer
from django.db.models import Count
from .models import Post
from .serializers import PostSerializer
from django.db.models import Subquery, OuterRef
from django.db import models

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_posts(request):
    likes_subquery = Like.objects.filter(post=OuterRef('pk')).values('post').order_by().annotate(count=Count('id')).values('count')
    comments_subquery = Comment.objects.filter(post=OuterRef('pk')).values('post').order_by().annotate(count=Count('id')).values('count')

    posts = Post.objects.annotate(
        likes_count=Subquery(likes_subquery, output_field=models.IntegerField()),
        comments_count=Subquery(comments_subquery, output_field=models.IntegerField())
    ).order_by('-likes_count')

    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_post(request: Request):
    user = request.user
    request.data['user'] = user.id
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    request.data['user_id'] = user.id
    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user_posts(request, pk):
    posts = Post.objects.filter(user_id=pk)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

