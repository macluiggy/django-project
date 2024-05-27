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
from posts.models import Post
from comments.models import Comment
from .serializers import CommentSerializer

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_comment(request: Request, post_id: int):
    post = get_object_or_404(Post, pk=post_id)
    data = {
        'post': post.id,
        'user': request.user.id,
        'content': request.data['content']
    }
    serializer = CommentSerializer(data=data)
    if serializer.is_valid():
        serializer.save(user=request.user, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def remove_comment(request, post_id):
    comment = get_object_or_404(Comment, pk=post_id, user=request.user)
    comment.delete()
    return Response({"detail": "Comment removed."}, status=status.HTTP_204_NO_CONTENT)
    