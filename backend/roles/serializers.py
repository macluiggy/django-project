from rest_framework import serializers
from country.models import Country
from .models import Role, UserRole
from area.serializers import AreaSerializer
from country.serializers import CountrySerializer
from permissions.serializers import RolePermissionSerializer
class RolesSerializer(serializers.ModelSerializer):
    country_id = serializers.IntegerField(write_only=True)
    country = CountrySerializer(many=False, read_only=True)
    role_permissions = RolePermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = '__all__'
        
class UserRolesSerializer(serializers.ModelSerializer):
    # role = RolesSerializer(read_only=True)
    # area = AreaSerializer(read_only=True)
    
    class Meta:
        model = UserRole
        fields = '__all__'
        