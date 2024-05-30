from rest_framework import serializers
from country.models import Country
from .models import Role, UserRole
from area.serializers import AreaSerializer
class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        
class UserRolesSerializer(serializers.ModelSerializer):
    role = RolesSerializer()
    area = AreaSerializer()
    
    class Meta:
        model = UserRole
        fields = '__all__'