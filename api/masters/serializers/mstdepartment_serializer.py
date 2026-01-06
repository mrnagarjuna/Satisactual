from rest_framework import serializers
from ..models import MstDepartments

class MstDepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstDepartments
        fields = '__all__'
