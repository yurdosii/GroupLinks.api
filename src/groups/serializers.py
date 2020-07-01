from rest_framework import serializers
from groups.models import Group, Link


class GroupBaseSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['name']
        model = Group
        fields = ('id', 'name', 'description', 'created')


class LinkBaseSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['id']
        model = Link
        fields = ('id', 'link', 'description', 'is_done', 'added')


class GroupWithNestedSerializer(GroupBaseSerializer):
    links = LinkBaseSerializer(many=True, read_only=True)

    class Meta(GroupBaseSerializer.Meta):
        fields = GroupBaseSerializer.Meta.fields + ('links', )


class LinkWithNestedSerializer(LinkBaseSerializer):
    groups = GroupBaseSerializer(many=True, read_only=True)

    class Meta(LinkBaseSerializer.Meta):
        fields = LinkBaseSerializer.Meta.fields + ('groups', )
