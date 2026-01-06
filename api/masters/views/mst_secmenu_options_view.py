from rest_framework import viewsets
from ..models import SecMenuOptions
from ..serializers.mst_secmenu_options_serializer import SecMenuOptionsSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet

class SecMenuOptionsViewSet(BaseModelViewSet):
    queryset = SecMenuOptions.objects.all()
    serializer_class = SecMenuOptionsSerializer
    permission_classes = [IsAuthenticated]
