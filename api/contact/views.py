from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,permissions
from .models import MstContactChannel,MstContactOutcome
from .serializer import MstContactChannelSerializer,MstContactOutcomeSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet

class MstContactChannelViewSet(BaseModelViewSet):
    queryset = MstContactChannel.objects.all()
    serializer_class = MstContactChannelSerializer
    permission_classes = [IsAuthenticated]

class MstContactOutcomeViewSet(BaseModelViewSet):
    queryset = MstContactOutcome.objects.all()
    serializer_class = MstContactOutcomeSerializer
    permission_classes = [IsAuthenticated]

# class MstContractEventsViewSet(BaseModelViewSet):
#     queryset = MstContractEvents.objects.all()
#     serializer_class = MstContractEventsSerializer
#     permission_classes = [IsAuthenticated]


# class MstContractTypesViewSet(BaseModelViewSet):
#     queryset = MstContractTypes.objects.all()
#     serializer_class = MstContractTypesSerializer
#     permission_classes = [IsAuthenticated]