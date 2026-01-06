from utils.services.baseviewset import BaseModelViewSet
from ..models import MstTimeZone
from ..serializers.mst_timezone_serializer import MstTimeZoneSerializer
from rest_framework.permissions import IsAuthenticated

class MstTimeZoneViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=MstTimeZone.objects.all()
    serializer_class=MstTimeZoneSerializer