from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from ..models import MstLanguages
from ..serializers.mst_language_serializer import MstLanguagesSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet


class MstLanguagesViewSet(BaseModelViewSet):
    queryset = MstLanguages.objects.all()
    serializer_class = MstLanguagesSerializer
    permission_classes = [IsAuthenticated]
