from authapp.Utils.decorators import cache_it
from authapp.models import Photos
from rest_framework.response import Response
from authapp.Photos.photos_serializer import PhotosSerializer


class PhotoInfoDAL:
    @staticmethod
    def get_selialized_data(photo_id):
        photo_info = PhotoInfoDAL.get_photo_info(photo_id)
        serialized_data = PhotosSerializer(photo_info, many=True)
        return Response(serialized_data.data)

    @staticmethod
    @cache_it(key_prefix="get_photo_info", timeout=30 * 24 * 60 * 60)
    def get_photo_info(photo_id):
        return Photos.objects.filter(photo_id=photo_id)
