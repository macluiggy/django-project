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
from .models import Like
from posts.models import Post
from .serializers import LikeSerializer
from permissions.permissions import HasPermissionToComment
# Create your views here.
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,  HasPermissionToComment])
def add_like(request: Request, pk: int):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if created:
        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def remove_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(user=request.user, post=post)
    if like.exists():
        like.delete()
        return Response({"detail": "Like removed."}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({"detail": "Like not found."}, status=status.HTTP_404_NOT_FOUND)
    