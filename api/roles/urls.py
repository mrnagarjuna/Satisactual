from rest_framework.routers import DefaultRouter
from .views import SecUserRolesViewSet,SecUserXRolesViewSet,SecUserRoleMenusListView,SecUserRoleDisclosuresListView
from django.urls import path, include

router = DefaultRouter()
router.register(r"mst-user-roles", SecUserRolesViewSet, basename="mstuserroles")
router.register(r"mst-user-x-roles",SecUserXRolesViewSet,basename="mstuserxroles")
router.register(r'mst-user-role-menus',SecUserRoleMenusListView,basename='mstuserrolemenus')
router.register(r'mst-user-role-disclosures',SecUserRoleDisclosuresListView,basename="mstuserroledisclosures")


urlpatterns = [
    path('', include(router.urls)),
]

