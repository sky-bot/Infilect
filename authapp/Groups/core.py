from authapp.models import Groups, Photos
from authapp.Utils.pagination import CustomPaginator
from authapp.Utils.decorators import cache_it


class GroupDAL:               # Data Access layer
    @staticmethod
    def get_all_paginated_groups(request):
        result = GroupDAL._get_all_groups()
        paginator = CustomPaginator(15)
        paginated_list = paginator.paginate_queryset(result, request)
        response = paginator.get_paginated_response(paginated_list)
        return response


    @staticmethod
    @cache_it(key_prefix="get_all_groups", timeout=30 * 24 * 60 * 60)  # 30days
    def _get_all_groups():
        return list(Groups.objects.all().values())


class GroupPhotoDAL:

    @staticmethod
    def get_paginated_photos(group_id, request):
        result = GroupPhotoDAL._get_all_photos_for_group(group_id)
        paginator = CustomPaginator(15)
        paginated_list = paginator.paginate_queryset(result, request)
        response = paginator.get_paginated_response(paginated_list)
        return response


    @staticmethod
    @cache_it(key_prefix="_get_all_photos_for_group", timeout=30 * 24 * 60 * 60)
    def _get_all_photos_for_group(group_id):
        return list(Photos.objects.filter(group_id=group_id).values())
