from rest_framework import serializers
from country.models import Country
from .models import Role
class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'