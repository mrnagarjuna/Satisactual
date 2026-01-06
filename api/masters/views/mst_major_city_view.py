# views.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound
from ..models import MstMajorCity
from ..serializers.mst_major_city_serializer import MstMajorCitySerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet


class MstMajorCityViewSet(BaseModelViewSet):
    queryset = MstMajorCity.objects.all()
    serializer_class = MstMajorCitySerializer
    permission_classes=[IsAuthenticated]

    
