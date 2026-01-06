from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from ..models import MstDisabilityCodes
from ..serializers.mst_disabilitycodes_serializer import MstDisabilityCodesSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet

class MstDisabilityCodesViewSet(BaseModelViewSet):
    queryset = MstDisabilityCodes.objects.all()
    serializer_class = MstDisabilityCodesSerializer
    permission_classes = [IsAuthenticated]

    # lookup_field = 'cod_disability'  # placeholder for DRF

    # def get_object(self):
    #     cod_disability = self.kwargs.get('cod_disability')
    #     cod_rec_status = self.kwargs.get('cod_rec_status')

    #     return get_object_or_404(
    #         MstDisabilityCodes,
    #         cod_disability=cod_disability,
    #         cod_rec_status=cod_rec_status
    #     )
