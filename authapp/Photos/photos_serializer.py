from rest_framework import serializers
from authapp.models import Photos


class PhotosSerializer(serializers.Serializer):
    photo_id = serializers.SerializerMethodField()
    owner_id = serializers.SerializerMethodField()
    server = serializers.SerializerMethodField()
    farm = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    is_public = serializers.SerializerMethodField()
    owner_name = serializers.SerializerMethodField()
    date_added = serializers.SerializerMethodField()
    group_id = serializers.SerializerMethodField()
    group_name = serializers.SerializerMethodField()
    group_description = serializers.SerializerMethodField()

    def get_photo_id(self, photo):
        return photo.photo_id

    def get_owner_id(self, photo):
        return photo.owner_id

    def get_server(self, photo):
        return photo.server

    def get_farm(self, photo):
        return photo.farm

    def get_title(self, photo):
        return photo.title

    def get_is_public(self, photo):
        return photo.is_public

    def get_owner_name(self, photo):
        return photo.owner_name

    def get_date_added(self, photo):
        return photo.date_added

    def get_group_id(self, photo):
        return photo.group.group_id

    def get_group_name(self, photo):
        return photo.group.group_name

    def get_group_description(self, photo):
        return photo.group.description

    class Meta:
        model = Photos
        fields = ('photo_id', 'owner_id', 'server', 'farm', 'title', 'is_public',
                  'owner_name', 'date_added', 'group_id', 'group_name',
                  'group_description')

