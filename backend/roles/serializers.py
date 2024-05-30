from rest_framework import serializers
from country.models import Country
from .models import Role, UserRole
from area.serializers import AreaSerializer
from country.serializers import CountrySerializer
from permissions.serializers import RolePermissionSerializer
class RolesSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    role_permissions = RolePermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = ['id', 'name', 'country', 'role_permissions']
        
class UserRolesSerializer(serializers.ModelSerializer):
    role = RolesSerializer()
    area = AreaSerializer()
    
    class Meta:
        model = UserRole
        fields = '__all__'