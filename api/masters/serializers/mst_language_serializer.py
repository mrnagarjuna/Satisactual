from rest_framework import serializers
from ..models import MstLanguages


class MstLanguagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = MstLanguages
        fields = '__all__'
