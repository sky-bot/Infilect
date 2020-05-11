
from rest_framework import viewsets

from authapp.Groups.core import GroupDAL


class GroupsViewSet(viewsets.ModelViewSet):
    def list(self, request, **kwargs):
        result = GroupDAL.get_all_paginated_groups(request)
        return result
