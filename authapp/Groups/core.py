from authapp.models import Groups, Photos
from authapp.Utils.pagination import CustomPaginator
from authapp.Groups.group_serializer import GroupSerializer
from authapp.Photos.photos_serializer import PhotosSerializer


class GroupDAL:               # Data Access layer
    @staticmethod
    def get_all_paginated_groups(request):
        result = Groups.objects.all().order_by('members')

        paginator = CustomPaginator(15)
        paginated_list = paginator.paginate_queryset(result, request)

        serialized_data = GroupSerializer(paginated_list, many=True)
        response = paginator.get_paginated_response(serialized_data.data)

        return response


class GroupPhotoDAL:

    @staticmethod
    def get_paginated_photos(group_id, request):
        result = Photos.objects.filter(group_id=group_id)

        paginator = CustomPaginator(15)
        paginated_list = paginator.paginate_queryset(result, request)

        serialized_data = PhotosSerializer(paginated_list, many=True)
        response = paginator.get_paginated_response(serialized_data.data)

        return response
