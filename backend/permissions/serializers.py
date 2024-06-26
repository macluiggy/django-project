from rest_framework import serializers
from .models import Permission
from .models import RolePermission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
        
class RolePermissionSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(read_only=True, many=True)
    class Meta:
        model = RolePermission
        fields = '__all__'