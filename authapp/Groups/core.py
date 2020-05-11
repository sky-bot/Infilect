from authapp.models import Groups, Photos
from authapp.Utils.pagination import CustomPaginator
from authapp.Utils.decorators import cache_it
from authapp.Groups.group_serializer import GroupSerializer
from authapp.Photos.photos_serializer import PhotosSerializer


class GroupDAL:               # Data Access layer
    @staticmethod
    def get_all_paginated_groups(request):
        result = GroupDAL.get_all_groups()
        paginator = CustomPaginator(15)
        paginated_list = paginator.paginate_queryset(result, request)
        serialized_data = GroupSerializer(paginated_list, many=True)
        response = paginator.get_paginated_response(serialized_data.data)
        return response


    @staticmethod
    @cache_it(key_prefix="get_all_groups", timeout=30 * 24 * 60 * 60)  # 30days
    def get_all_groups():
        return Groups.objects.all().order_by('members')


class GroupPhotoDAL:

    @staticmethod
    def get_paginated_photos(group_id, request):
        result = GroupPhotoDAL._get_all_photos_for_group(group_id)
        paginator = CustomPaginator(15)
        paginated_list = paginator.paginate_queryset(result, request)
        serialized_data = PhotosSerializer(paginated_list, many=True)
        response = paginator.get_paginated_response(serialized_data.data)
        return response


    @staticmethod
    @cache_it(key_prefix="_get_all_photos_for_group", timeout=30 * 24 * 60 * 60)
    def _get_all_photos_for_group(group_id):
        return Photos.objects.filter(group_id=group_id)
