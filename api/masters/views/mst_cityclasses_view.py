from rest_framework import viewsets
from ..models import MstCityClasses
from ..serializers.mst_cityclasses_serializer import MstCityClassesSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet

class MstCityClassesViewSet(BaseModelViewSet):
    queryset = MstCityClasses.objects.all()
    serializer_class = MstCityClassesSerializer
    permission_classes = [IsAuthenticated]
