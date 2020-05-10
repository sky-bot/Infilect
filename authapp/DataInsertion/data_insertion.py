from rest_framework.views import APIView
from authapp.models import Groups, Photos
from rest_framework.response import Response
from datetime import datetime


# todo is authenticated decorator
class DataInsertion(APIView):

    def post(self, request):
        group_id = request.data.get('group_id')
        group_name = request.data.get('group_name')
        all_photos = request.data.get('photos')

        group = Groups(group_id=group_id, group_name=group_name)
        group.save()

        for pic in all_photos:
            timestamp = pic.get('dateadded')
            time = datetime.fromtimestamp(int(timestamp))
            photo = Photos(photo_id=pic.get('id'), owner_id=pic.get('owner'),
                           server=pic.get('server'), farm=pic.get('farm'),
                           title=pic.get('title'), is_public=pic.get('ispublic'),
                           owner_name=pic.get('ownername'), date_added=time,
                           group=group)
            photo.save()

        return Response({'detail': "Success"})
