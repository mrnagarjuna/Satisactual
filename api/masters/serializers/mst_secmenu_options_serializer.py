from rest_framework import serializers
from ..models import SecMenuOptions

class SecMenuOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecMenuOptions
        fields = '__all__'
