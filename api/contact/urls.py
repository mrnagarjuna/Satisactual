from rest_framework import routers
from django.urls import path, include
from .views import MstContactChannelViewSet,MstContactOutcomeViewSet

router = routers.DefaultRouter()
router.register(r'mst-contact-channels', MstContactChannelViewSet,basename='contactchannels')
router.register(r'mst-contact-outcomes', MstContactOutcomeViewSet,basename='mstcontactoutcome')
# router.register(r'mstcontract-events', MstContractEventsViewSet,basename='mstcontractevent')
# router.register(r'mst-contract-types', MstContractTypesViewSet,basename='mstcontracttypes')

urlpatterns = [
    path('', include(router.urls)),
]
