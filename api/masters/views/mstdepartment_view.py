from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from ..models import MstDepartments
from ..serializers.mstdepartment_serializer import MstDepartmentsSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet

class MstDepartmentsViewSet(BaseModelViewSet):
    queryset = MstDepartments.objects.all()
    serializer_class = MstDepartmentsSerializer
    permission_classes = [IsAuthenticated]

    # lookup_field = 'cod_department'  # placeholder for DRF

    # def get_object(self):
    #     cod_department = self.kwargs.get('cod_department')
    #     id_third_party = self.kwargs.get('id_third_party')
    #     cod_rec_status = self.kwargs.get('cod_rec_status')

    #     return get_object_or_404(
    #         MstDepartments,
    #         cod_department=cod_department,
    #         id_third_party=id_third_party,
    #         cod_rec_status=cod_rec_status
    #     )
