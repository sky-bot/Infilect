from django.urls import path, include
from authapp import views
from authapp.DataInsertion import DataInsertion
from authapp.Groups import GroupInfo, GroupPhoto

urlpatterns = [
    # for Auth
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),

    # for Data population
    path('group-data', DataInsertion.as_view()),

    path('groups', GroupInfo.as_view()),
    path('group/<str:group_id>', GroupPhoto.as_view())
]
