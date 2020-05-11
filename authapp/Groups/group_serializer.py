from rest_framework import serializers
from authapp.models import Groups


class GroupSerializer(serializers.Serializer):
    group_id = serializers.SerializerMethodField()
    group_name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    rules = serializers.SerializerMethodField()
    members = serializers.SerializerMethodField()
    pool_count = serializers.SerializerMethodField()

    def get_group_id(self, group):
        return group.group_id

    def get_group_name(self, group):
        return group.group_name

    def get_description(self, group):
        return group.description

    def get_rules(self, group):
        return group.rules

    def get_members(self, group):
        return group.members

    def get_pool_count(self, group):
        return group.pool_count

    class Meta:
        model = Groups
        fields = ('group_id', 'group_name', 'description', 'rules', 'members', 'pool_count')
