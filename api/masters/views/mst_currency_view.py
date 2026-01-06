from rest_framework import viewsets
from ..models import MstCurrency
from ..serializers.mst_currency_serializer import MstCurrencySerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet

class MstCurrencyViewSet(BaseModelViewSet):
    queryset = MstCurrency.objects.all()
    serializer_class = MstCurrencySerializer
    permission_classes = [IsAuthenticated]
