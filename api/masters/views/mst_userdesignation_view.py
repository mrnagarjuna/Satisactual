# views.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound
from ..models import MstUserDesignation
from ..serializers.mst_userdesignation_serializer import MstUserDesignationSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet


class MstUserDesignationViewSet(BaseModelViewSet):
    queryset = MstUserDesignation.objects.all()
    serializer_class = MstUserDesignationSerializer
    permission_classes = [IsAuthenticated]

