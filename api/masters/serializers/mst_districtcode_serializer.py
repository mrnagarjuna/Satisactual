from rest_framework import serializers
from ..models import MstDistrictCodes

class MstDistrictCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstDistrictCodes
        fields = "__all__"
