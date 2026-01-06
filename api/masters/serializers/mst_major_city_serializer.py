
# serializers.py
from rest_framework import serializers
from ..models import MstMajorCity


class MstMajorCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MstMajorCity
        fields = "__all__"
