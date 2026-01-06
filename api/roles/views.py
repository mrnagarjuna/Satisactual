from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SecUserRoles,SecUserXRoles,SecUserRoleMenus,SecUserRoleDisclosures
from .serializer import SecUserRolesSerializer,SecUserXRolesSerializer,SecUserRoleMenusSerializer,SecUserRoleDisclosuresSerializer
from utils.services.baseviewset import BaseModelViewSet


class SecUserRolesViewSet(BaseModelViewSet):
    queryset = SecUserRoles.objects.all()
    serializer_class = SecUserRolesSerializer
    permission_classes = [IsAuthenticated]

class SecUserXRolesViewSet(BaseModelViewSet):
    queryset = SecUserXRoles.objects.all()
    serializer_class = SecUserXRolesSerializer
    permission_classes = [IsAuthenticated]


class SecUserRoleMenusListView(BaseModelViewSet):
    queryset = SecUserRoleMenus.objects.all().order_by(
        "cod_user_role",
        "num_display_order"
    )
    serializer_class = SecUserRoleMenusSerializer

class SecUserRoleDisclosuresListView(BaseModelViewSet):
    queryset = SecUserRoleDisclosures.objects.all().order_by(
        "cod_user_role",
        "num_sequence"
    )
    serializer_class = SecUserRoleDisclosuresSerializer



