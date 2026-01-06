from rest_framework import serializers
from ..models import MstCurrency

class MstCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = MstCurrency
        fields = '__all__'
