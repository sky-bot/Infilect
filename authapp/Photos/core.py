from authapp.Utils.decorators import cache_it
from authapp.models import Photos

from authapp.Photos.photos_serializer import PhotosSerializer


class PhotoInfoDAL:
    @staticmethod
    @cache_it(key_prefix="get_photo_info", timeout=30 * 24 * 60 * 60)
    def get_selialized_data(photo_id):
        if not isinstance(photo_id, int):
            photo_id = int(photo_id)
        photo_info = Photos.objects.filter(photo_id=photo_id)
        serialized_data = PhotosSerializer(photo_info, many=True)
        return serialized_data.data
