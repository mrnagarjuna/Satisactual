from rest_framework import serializers
from ..models import MstAddrTypes

class MstAddrTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstAddrTypes
        fields = '__all__'
