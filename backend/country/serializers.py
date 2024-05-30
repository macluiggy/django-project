from rest_framework import serializers
from country.models import Country
from django.contrib.auth.models import User

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'