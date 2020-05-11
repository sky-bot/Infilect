from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.versioning import URLPathVersioning
from authapp.Groups.core import GroupPhotoDAL
from authapp.Photos.core import PhotoInfoDAL


@permission_classes([IsAuthenticated])
class GroupPhotoViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        result = PhotoInfoDAL.get_selialized_data(pk)
        return Response(result)

    def list(self, request, **kwargs):
        group_id = request.GET.get('group')
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
