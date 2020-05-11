from django.urls import path, include
from rest_framework import routers

from authapp.Groups import GroupPhotoViewSet, SingleGroupViewSet, GroupsViewSet

router = routers.SimpleRouter()
router.register(r'groups', GroupsViewSet, basename="groups-Info")
router.register(r'photos', GroupPhotoViewSet, basename="all-group-photos")
router.register(r'group', SingleGroupViewSet, basename="single-group")

urlpatterns = [
    # #for Auth
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]

urlpatterns += router.urls
