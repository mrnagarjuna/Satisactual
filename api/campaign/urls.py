from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MstCampaignTypesViewSet,MstCampaignTeamRoleViewSet,MstThirdPartyTypesViewSet,MstThirdPartiesViewSet,CmpCampaignsViewSet,CmpCampaignUserGeoCoverageViewSet

router = DefaultRouter()

router.register(r'mst-campaign-types', MstCampaignTypesViewSet, basename='mstcampaigntypes')
router.register(r'mst-campaign-teamrole',MstCampaignTeamRoleViewSet,basename='mstcampaignteamrole')
router.register(r'mst-third-party-types',MstThirdPartyTypesViewSet,basename='mst-third-party-types')
router.register(r'mst-third-party',MstThirdPartiesViewSet,basename='mst-third-party')
router.register(r'mst-campaign',CmpCampaignsViewSet,basename='mst-campaign')
router.register(r'Cmp-Campaign-User-GeoCoverage',CmpCampaignUserGeoCoverageViewSet,basename='Cmp-Campaign-User-GeoCoverage')


urlpatterns = [
    path('', include(router.urls)),
]
