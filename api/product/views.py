from django.shortcuts import render
from utils.services.baseviewset import BaseModelViewSet
from .models import MstProdCodes,MstProdDisclosures,MstProdDocs,MstPromoCodes
from .serializers import MstProdCodesSerializer,MstProdDisclosuresSerializer,MstProdDocsSerializer,MstPromoCodesSerializer
from rest_framework.permissions import IsAuthenticated

class MstProdCodesViewset(BaseModelViewSet):
    queryset=MstProdCodes.objects.all()
    serializer_class=MstProdCodesSerializer
    permission_classes=[IsAuthenticated]

class MstProdDisclosuresViewSet(BaseModelViewSet):
    queryset = MstProdDisclosures.objects.all()
    serializer_class = MstProdDisclosuresSerializer
    permission_classes = [IsAuthenticated]

class MstProdDocsViewSet(BaseModelViewSet):
    queryset = MstProdDocs.objects.all()
    serializer_class = MstProdDocsSerializer
    permission_classes = [IsAuthenticated]

class MstPromoCodesViewSet(BaseModelViewSet):
    queryset = MstPromoCodes.objects.all()
    serializer_class = MstPromoCodesSerializer
    permission_classes = [IsAuthenticated]