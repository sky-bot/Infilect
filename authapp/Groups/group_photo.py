from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from authapp.Photos.core import PhotoInfoDAL
from authapp.Photos.photos_serializer import PhotosSerializer
from authapp.Groups.group_serializer import GroupSerializer
from authapp.Groups.core import GroupPhotoDAL, GroupDAL
from rest_framework.response import Response
from rest_framework import viewsets

from authapp.models import Photos, Groups


class GroupPhoto(APIView):
    def get(self, request, *args, **kwargs):
        group_id = kwargs.get('group_id') or request.GET.get('group')
        if not group_id:
            raise ValidationError(detail="Input not provided")

        result = GroupPhotoDAL.get_paginated_photos(group_id, request)

        return result


class GroupPhotoViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        result = PhotoInfoDAL.get_selialized_data(pk)
        return result

    def list(self, request, **kwargs):
        group_id = kwargs.get('group_id') or request.GET.get('group_id')
        if not group_id:
            raise ValidationError(detail="Input not provided")

        result = GroupPhotoDAL.get_paginated_photos(group_id, request)

        return result


class SingleGroupViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        group_id = pk
        if not group_id:
            raise ValidationError(detail="Input not provided")

        result = GroupPhotoDAL.get_paginated_photos(group_id, request)

        return result


        result = PhotoInfoDAL.get_selialized_data(pk)
        return result