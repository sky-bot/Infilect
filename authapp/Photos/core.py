from authapp.Utils.decorators import cache_it
from authapp.models import Photos
from rest_framework.response import Response


class PhotoInfoDAL:
    @staticmethod
    def get_photo_info(photo_id):
        photo_info = Photos.objects.get(photo_id=photo_id)
        result = PhotoInfoDAL.get_formatted_data(photo_info)
        return Response(result)

    @staticmethod
    @cache_it(key_prefix="get_formatted_data", timeout=30 * 24 * 60 * 60)
    def get_formatted_data(photo_obj):
        temp_dict = {
            'photo_id': photo_obj.photo_id,
            'owner_id': photo_obj.owner_id,
            'server': photo_obj.server,
            'farm': photo_obj.title,
            'is_public': photo_obj.is_public,
            'owner_name': photo_obj.owner_name,
            'date_added': photo_obj.date_added,
            'group_id': photo_obj.group.group_id,
            'group_name': photo_obj.group.group_name,
            'group_description': photo_obj.group.description
        }
        return temp_dict
