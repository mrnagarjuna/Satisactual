from utils.services.baseviewset import BaseModelViewSet
from ..models import MstPinCodes
from ..serializers import mst_pincodes_serializer
from rest_framework.permissions import IsAuthenticated

class MstPinCodesViewSet(BaseModelViewSet):
    queryset = MstPinCodes.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class=mst_pincodes_serializer.MstPinCodesSerializer
    