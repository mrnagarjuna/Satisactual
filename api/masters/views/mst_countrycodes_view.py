from rest_framework import viewsets
from ..models import MstCountryCodes
from ..serializers.mst_countrycodes_serializer import MstCountryCodesSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet

class MstCountryCodesViewSet(BaseModelViewSet):
    queryset = MstCountryCodes.objects.all()
    serializer_class = MstCountryCodesSerializer
    permission_classes = [IsAuthenticated]
