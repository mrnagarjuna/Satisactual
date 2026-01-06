from rest_framework import viewsets
from ..models import MstCreditOfficerLevels
from ..serializers.mst_credit_officerlevels_serializer import MstCreditOfficerLevelsSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet

class MstCreditOfficerLevelsViewSet(BaseModelViewSet):
    queryset = MstCreditOfficerLevels.objects.all()
    serializer_class = MstCreditOfficerLevelsSerializer
    permission_classes = [IsAuthenticated]
