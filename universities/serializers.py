from rest_framework import serializers
from .models import Institutions, Zipcodes

class ZipcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zipcodes
        fields = '__all__'

class InstitutionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institutions
        fields = '__all__'
        depth = 2