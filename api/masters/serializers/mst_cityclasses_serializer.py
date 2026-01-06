from rest_framework import serializers
from ..models import MstCityClasses

class MstCityClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstCityClasses
        fields = '__all__'
