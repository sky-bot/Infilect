from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from authapp.Groups.core import GroupPhotoDAL
from authapp.Photos.core import PhotoInfoDAL


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
