from rest_framework import serializers
from .models import MstQuestionClass,MstQuestionType


class MstQuestionClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstQuestionClass
        fields = "__all__"


class MstQuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstQuestionType
        fields = "__all__"
