"""
API serializers
"""

from rest_framework import serializers
from groups.models import Group, Link


class GroupBaseSerializer(serializers.ModelSerializer):
    """
    Group base serializer
    """
    class Meta:
        ordering = ['name']
        model = Group
        fields = ('id', 'name', 'description', 'created')


class LinkBaseSerializer(serializers.ModelSerializer):
    """
    Link base serializer (for nesting in Group)
    """
    isDone = serializers.BooleanField(source='is_done')

    class Meta:
        ordering = ['id']
        model = Link
        fields = ('id', 'url', 'description', 'isDone', 'added')


class GroupWithNestedSerializer(GroupBaseSerializer):
    """
    Group serializer with nested links
    """
    links = LinkBaseSerializer(many=True, read_only=True)

    class Meta(GroupBaseSerializer.Meta):
        fields = GroupBaseSerializer.Meta.fields + ('links', )


class LinkWithNestedSerializer(LinkBaseSerializer):
    """
    Link serializer with nested group
    """
    # groups = GroupBaseSerializer(many=True)
    # (треба щоб коли вводжу то міг вводити лише id групи, а коли виводжу то виводило все)

    class Meta(LinkBaseSerializer.Meta):
        fields = LinkBaseSerializer.Meta.fields + ('groups', )
