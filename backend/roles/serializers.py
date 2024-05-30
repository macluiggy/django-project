from rest_framework import serializers
from country.models import Country
from .models import Role, UserRole
class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        
class UserRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'