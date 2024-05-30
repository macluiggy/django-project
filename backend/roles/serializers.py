from rest_framework import serializers
from country.models import Country
from .models import Role, UserRole
from area.serializers import AreaSerializer
from country.serializers import CountrySerializer
class RolesSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    class Meta:
        model = Role
        fields = '__all__'
        
class UserRolesSerializer(serializers.ModelSerializer):
    role = RolesSerializer()
    area = AreaSerializer()
    
    class Meta:
        model = UserRole
        fields = '__all__'