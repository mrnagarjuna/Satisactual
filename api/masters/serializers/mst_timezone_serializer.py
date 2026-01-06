from rest_framework import serializers
from ..models import MstTimeZone


class MstTimeZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstTimeZone
        fields = "__all__"
