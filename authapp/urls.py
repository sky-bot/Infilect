from django.urls import path, include
from authapp import views
from authapp.DataInsertion import DataInsertion
from authapp.Groups import GroupInfo, GroupPhoto
from authapp.Photos import PhotoInfo
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
    # for Auth
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),

    # for Data population
    path('group-data', DataInsertion.as_view()),

    path('groups', GroupInfo.as_view()),                     # 2
    path('group/<str:group_id>', GroupPhoto.as_view()),      # 3
    path('photos', GroupPhoto.as_view()),                    # 4
    path('photos/<int:photo_id>', PhotoInfo.as_view()),      # 5
]
