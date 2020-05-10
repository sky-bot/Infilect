from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from authapp.Groups.core import GroupPhotoDAL


class GroupPhoto(APIView):
    def get(self, request, *args, **kwargs):
        group_id = kwargs.get('group_id') or request.get('group')
        if not group_id:
            raise ValidationError(detail="Input not provided")

        result = GroupPhotoDAL.get_paginated_photos(group_id, request)

        return result
