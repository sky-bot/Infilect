
from rest_framework import viewsets
from rest_framework.response import Response
from authapp.Photos.core import PhotoInfoDAL


class PhotoInfoViewSet(viewsets.ModelViewSet):

    def list(self, request, **kwargs):
        photo_id = kwargs.get('photo_id')
        result = PhotoInfoDAL.get_selialized_data(photo_id)
        return Response(result)
