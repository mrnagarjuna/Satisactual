from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import MstQuestionClass,MstQuestionType
from .serializers import MstQuestionClassSerializer,MstQuestionTypeSerializer
from utils.services.baseviewset import BaseModelViewSet


class MstQuestionClassViewSet(BaseModelViewSet):
    queryset = MstQuestionClass.objects.all()
    serializer_class = MstQuestionClassSerializer
    permission_classes = [IsAuthenticated]

class MstQuestionTypeViewSet(BaseModelViewSet):
    queryset = MstQuestionType.objects.all()
    serializer_class = MstQuestionTypeSerializer
    permission_classes = [IsAuthenticated]