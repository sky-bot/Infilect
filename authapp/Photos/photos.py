from rest_framework.views import APIView

from authapp.Photos.core import PhotoInfoDAL


class PhotoInfo(APIView):
    def get(self, request, **kwargs):
        photo_id = kwargs.get('photo_id')
        result = PhotoInfoDAL.get_selialized_data(photo_id)
        return result
