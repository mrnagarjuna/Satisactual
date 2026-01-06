from rest_framework import viewsets
from ..models import MstDistrictCodes
from ..serializers.mst_districtcode_serializer import MstDistrictCodesSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet

class MstDistrictCodesViewSet(BaseModelViewSet):
    queryset = MstDistrictCodes.objects.all()
    serializer_class = MstDistrictCodesSerializer
    permission_classes = [IsAuthenticated]
    # lookup_field = 'cod_district'
