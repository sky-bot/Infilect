from django.urls import path, include
from authapp import views
from authapp.DataInsertion import DataInsertion
from authapp.Groups import GroupInfo, GroupPhoto
from authapp.Groups.group_photo import GroupPhotoViewSet, SingleGroupViewSet
from authapp.Photos import PhotoInfo
from rest_framework import routers
from authapp.Groups.groups import GroupsViewSet
from authapp.Photos.photos import PhotoInfoViewSet

router = routers.SimpleRouter()
router.register(r'groups', GroupsViewSet, basename="groups-Info")
router.register(r'photos', GroupPhotoViewSet, basename="all-group-photos")
router.register(r'group', SingleGroupViewSet, basename="single-group")
# router.register(r'photos/', PhotoInfoViewSet, basename="photo-info")

urlpatterns = [
    # #for Auth
    # path('', include('djoser.urls')),
    # path('', include('djoser.urls.authtoken')),
    #
    # # for Data population
    # path('group-data', DataInsertion.as_view()),
    #
    # # for Task
    # path('groups', GroupInfo.as_view()),                     # 2   #done
    # path('group/<str:group_id>', GroupPhoto.as_view()),      # 3
    # path('photos', GroupPhoto.as_view()),                    # 4   #done
    # path('photos/<int:photo_id>', PhotoInfo.as_view()),      # 5   #done
]

urlpatterns += router.urls