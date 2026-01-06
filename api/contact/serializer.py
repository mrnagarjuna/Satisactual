from rest_framework import serializers
from .models import MstContactChannel,MstContactOutcome

class MstContactChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstContactChannel
        fields = "__all__"

class MstContactOutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstContactOutcome
        fields = "__all__"

# class MstContractEventsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MstContractEvents
#         fields = "__all__"

# class MstContractTypesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MstContractTypes
#         fields = "__all__"



