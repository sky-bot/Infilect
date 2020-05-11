from rest_framework.views import APIView
from rest_framework import viewsets

from authapp.Photos.core import PhotoInfoDAL
from authapp.models import Photos


class PhotoInfo(APIView):
    def get(self, request, **kwargs):
        photo_id = kwargs.get('photo_id')
        result = PhotoInfoDAL.get_selialized_data(photo_id)
        return result


class PhotoInfoViewSet(viewsets.ModelViewSet):
    def get_queryset(self, photo_id=None):
        Photos.objects.filter(photo_id=photo_id)

    def list(self, request, **kwargs):
        photo_id = kwargs.get('photo_id')
        result = PhotoInfoDAL.get_selialized_data(photo_id)
        return result
