from rest_framework import serializers
from ..models import MstPinCodes

class MstPinCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstPinCodes
        fields = '__all__'