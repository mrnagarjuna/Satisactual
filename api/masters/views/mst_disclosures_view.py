from rest_framework import viewsets
from ..models import MstDisclosures
from ..serializers.mst_disclosures_serializer import MstDisclosuresSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet

class MstDisclosuresViewSet(BaseModelViewSet):
    queryset = MstDisclosures.objects.all()
    serializer_class = MstDisclosuresSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     qs = MstDisclosures.objects.all()
    #     cod_disclosure = self.kwargs.get("cod_disclosure")
    #     cod_rec_status = self.kwargs.get("cod_rec_status")

    #     if cod_disclosure:
    #         qs = qs.filter(cod_disclosure=cod_disclosure)

    #     if cod_rec_status:
    #         qs = qs.filter(cod_rec_status=cod_rec_status)

    #     return qs
