from rest_framework import serializers
from .models import MstCampaignTypes,MstCampaignTeamRole,MstThirdPartyTypes,MstThirdParties,CmpCampaigns,CmpCampaignUserGeoCoverage
from ..masters.serializers.mstdepartment_serializer import MstDepartmentsSerializer

class MstCampaignTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstCampaignTypes
        fields = "__all__"


class MstCampaignTeamRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstCampaignTeamRole
        fields = '__all__'

class MstThirdPartyTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstThirdPartyTypes
        fields = '__all__'
    
class MstThirdPartyTypesCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstThirdPartyTypes
        exclude = ('dat_last_maker', 'dat_last_checker')

class MstThirdPartiesSerializer(serializers.ModelSerializer):
    departments = MstDepartmentsSerializer(many=True, read_only=True)
    class Meta:
        model = MstThirdParties
        fields = '__all__'

class CmpCampaignsSerializer(serializers.ModelSerializer):
    bin_logo_to_display = serializers.ImageField(required=False, allow_null=True)
    class Meta:
        model = CmpCampaigns
        fields = "__all__"
        
        
class CmpCampaignUserGeoCoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model=CmpCampaignUserGeoCoverage
        fields="__all__"