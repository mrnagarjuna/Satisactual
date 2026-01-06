# serializers.py
from rest_framework import serializers
from ..models import MstUserDesignation


class MstUserDesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstUserDesignation
        fields = "__all__"
