from rest_framework import serializers
from ..models import MstCountryCodes

class MstCountryCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstCountryCodes
        fields = '__all__'
