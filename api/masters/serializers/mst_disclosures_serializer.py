from rest_framework import serializers
from ..models import MstDisclosures

class MstDisclosuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstDisclosures
        fields = '__all__'
