from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets, permissions
from .models import SecUserMaster,SecUserPswdHist
from .serializer import SecUserMasterSerializer,SecUserPswdHistCreateSerializer,SecUserPswdHistSerializer

from rest_framework import status, viewsets
from utils.services.responses import success_response, error_response
from utils.services.baseviewset import BaseModelViewSet





class SecUserMasterViewSet(BaseModelViewSet):
    """
    API endpoint for SecUserMaster.
    Password (txt_user_signature) is write-only and won't be visible in GET responses.
    """
    queryset = SecUserMaster.objects.all()
    serializer_class = SecUserMasterSerializer
    #permission_classes = [permissions.IsAuthenticated]  # or customize as needed

    # Optional: filter/queryset customization
    # def get_queryset(self):
    #     return SecUserMaster.objects.filter(is_active=True)

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import SecUserPreferences,SecUserAccessLog
from .serializer import SecUserPreferencesSerializer,SecUserAccessLogSerializer


class SecUserPreferencesViewSet(BaseModelViewSet):
    queryset = SecUserPreferences.objects.select_related('txt_login_id')
    serializer_class = SecUserPreferencesSerializer
    permission_classes = [IsAuthenticated]

class SecUserAccessLogListView(BaseModelViewSet):
    queryset = SecUserAccessLog.objects.all().order_by('-dat_time_login')
    serializer_class = SecUserAccessLogSerializer

class SecUserPswdHistViewSet(BaseModelViewSet):
    queryset = SecUserPswdHist.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return SecUserPswdHistCreateSerializer
        return SecUserPswdHistSerializer

