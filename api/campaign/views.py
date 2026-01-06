from rest_framework import status, viewsets,permissions
from .models import MstCampaignTypes, MstCampaignTeamRole,MstThirdPartyTypes,MstThirdParties,CmpCampaigns,CmpCampaignUserGeoCoverage
from .serializer import MstCampaignTypesSerializer, MstCampaignTeamRoleSerializer,MstThirdPartyTypesCreateUpdateSerializer,MstThirdPartyTypesSerializer,MstThirdPartiesSerializer,CmpCampaignsSerializer,CmpCampaignUserGeoCoverageSerializer
from utils.services.responses import success_response  # adjust path if needed
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class MstCampaignTypesViewSet(viewsets.ModelViewSet):
    queryset = MstCampaignTypes.objects.all()
    serializer_class = MstCampaignTypesSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        data = self.get_serializer(self.get_queryset(), many=True).data
        return success_response(
            message="Campaign types fetched successfully",
            data=data,
            status_code=status.HTTP_200_OK
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return success_response(
            message="Campaign type created successfully",
            data=serializer.data,
            status_code=status.HTTP_201_CREATED
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = self.get_serializer(instance).data
        return success_response(
            message="Campaign type retrieved successfully",
            data=data,
            status_code=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return success_response(
            message="Campaign type updated successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return success_response(
            message="Campaign type deleted successfully",
            data=None,
            status_code=status.HTTP_204_NO_CONTENT
        )


class MstCampaignTeamRoleViewSet(viewsets.ModelViewSet):
    queryset = MstCampaignTeamRole.objects.all()
    serializer_class = MstCampaignTeamRoleSerializer
    permission_classes = [IsAuthenticated]
    

    def list(self, request, *args, **kwargs):
        data = self.get_serializer(self.get_queryset(), many=True).data
        return success_response(
            message="Campaign team roles fetched successfully",
            data=data,
            status_code=status.HTTP_200_OK
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return success_response(
            message="Campaign team role created successfully",
            data=serializer.data,
            status_code=status.HTTP_201_CREATED
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = self.get_serializer(instance).data
        return success_response(
            message="Campaign team role retrieved successfully",
            data=data,
            status_code=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return success_response(
            message="Campaign team role updated successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return success_response(
            message="Campaign team role deleted successfully",
            data=None,
            status_code=status.HTTP_204_NO_CONTENT
        )

class MstThirdPartyTypesViewSet(BaseModelViewSet):
    queryset = MstThirdPartyTypes.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return MstThirdPartyTypesCreateUpdateSerializer
        return MstThirdPartyTypesSerializer
    
class MstThirdPartiesViewSet(BaseModelViewSet):
    queryset = MstThirdParties.objects.prefetch_related('departments')
    serializer_class = MstThirdPartiesSerializer
    permission_classes = [IsAuthenticated]

class CmpCampaignsViewSet(BaseModelViewSet):
    queryset = CmpCampaigns.objects.all()
    serializer_class = CmpCampaignsSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    @swagger_auto_schema(
        request_body=None,
        consumes=["multipart/form-data"],
        manual_parameters=[
            openapi.Parameter(
                'bin_logo_to_display',
                openapi.IN_FORM,
                description="Campaign logo",
                type=openapi.TYPE_FILE,
                required=False
            ),
            openapi.Parameter(
                'txt_campaign_name',
                openapi.IN_FORM,
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                'txt_campaign_title',
                openapi.IN_FORM,
                type=openapi.TYPE_STRING,
                required=False
            ),
            openapi.Parameter(
                'dat_start',
                openapi.IN_FORM,
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATE
            ),
            openapi.Parameter(
                'dat_end',
                openapi.IN_FORM,
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATE
            ),
        ]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class CmpCampaignUserGeoCoverageViewSet(BaseModelViewSet):
    queryset=CmpCampaignUserGeoCoverage.objects.all()
    serializer_class=CmpCampaignUserGeoCoverageSerializer
    permission_classes=[IsAuthenticated]