from rest_framework import serializers
from ..models import MstDisabilityCodes

class MstDisabilityCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstDisabilityCodes
        fields = '__all__'
