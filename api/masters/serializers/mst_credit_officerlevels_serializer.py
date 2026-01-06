from rest_framework import serializers
from ..models import MstCreditOfficerLevels

class MstCreditOfficerLevelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstCreditOfficerLevels
        fields = '__all__'
