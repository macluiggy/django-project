from gc import get_objects
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sympy import true

from roles.models import UserRole, Role
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from roles.serializers import UserRolesSerializer
from area.models import Area

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    
    if not user.check_password(request.data['password']):
        return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    
        
    area = request.data['area']
    # verify if the area exists
    area = get_object_or_404(Area, pk=area)
    role = request.data['role']
    # verify if the role exists
    role = get_object_or_404(Role, pk=role)
    
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        
        token = Token.objects.create(user=user)
        user_roles_serializer_data = { 'user': user.id, 'area': area, 'role': role }
        user_roles_serializer = UserRolesSerializer(data=user_roles_serializer_data)
        if user_roles_serializer.is_valid():
            user_roles_serializer.save()
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    return Response({'token': ' 1234'})

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    print(request.user)
    serializer = UserSerializer(instance=request.user)
    return Response('You are login as {}'.format(request.user.username), status=status.HTTP_200_OK)
    # return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user_roles(request):
    user_id = request.user.id
    user = get_object_or_404(User, pk=user_id)
    user_roles = UserRole.objects.filter(user=user)
    serializer = UserRolesSerializer(user_roles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)