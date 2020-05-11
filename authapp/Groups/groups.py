from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from authapp.Groups.core import GroupDAL


@permission_classes([IsAuthenticated])
class GroupsViewSet(viewsets.ModelViewSet):
    def list(self, request, **kwargs):
        result = GroupDAL.get_all_paginated_groups(request)
        return result
