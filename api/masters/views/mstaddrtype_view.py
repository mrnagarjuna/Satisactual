from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import MstAddrTypes
from ..serializers.mstaddrtypes_serializer import MstAddrTypesSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet

class MstAddrTypesViewSet(BaseModelViewSet):
    queryset = MstAddrTypes.objects.all()
    serializer_class = MstAddrTypesSerializer
    permission_classes = [IsAuthenticated]

    # Disable standard pk lookup since we have composite keys
    # lookup_field = 'cod_addr_type'
    # lookup_url_kwarg = 'cod_addr_type'
    # lookup_value_regex = '[^/]+'

    # def get_object(self):
    #     cod_addr_type = self.kwargs.get('cod_addr_type')
    #     # cod_rec_status = self.kwargs.get('cod_rec_status')

    #     return get_object_or_404(
    #         MstAddrTypes,
    #         cod_addr_type=cod_addr_type,
    #         # cod_rec_status=cod_rec_status
    #     )
    

