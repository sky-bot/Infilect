from rest_framework.views import APIView
from authapp.Groups.core import GroupDAL


class GroupInfo(APIView):
    def get(self, request):
        result = GroupDAL.get_all_paginated_groups(request)
        return result


