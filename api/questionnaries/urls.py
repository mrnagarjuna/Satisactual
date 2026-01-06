from rest_framework.routers import DefaultRouter
from .views import MstQuestionClassViewSet,MstQuestionTypeViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'mst-question-classes',MstQuestionClassViewSet,basename='mst-question-classes')
router.register(r'mst-question-types',MstQuestionTypeViewSet,basename='mstquestiontypes')

urlpatterns = [
    path('', include(router.urls)),
]
