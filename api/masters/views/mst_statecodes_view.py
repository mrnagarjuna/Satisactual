from rest_framework import serializers
from ..models import MstStateCodes
from ..serializers.mst_statecodes_serializer import MstStateCodesSerializer,MstStateCodesCreateSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet

class MstStateCodesViewSet(BaseModelViewSet):
    queryset = MstStateCodes.objects.all()
    permission_classes = [IsAuthenticated]
    

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return MstStateCodesCreateSerializer
        return MstStateCodesSerializer

