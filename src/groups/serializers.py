"""
API serializers
"""

from rest_framework import serializers
from groups.models import CustomUser, Group, Link


class CustomUserSerializer(serializers.ModelSerializer):
    """
    CustomUser serializer
    """
    class Meta:
        ordering = ['name']
        model = CustomUser
        fields = ('id', 'username', 'email', 'date_joined')


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
    owner = CustomUserSerializer(read_only=True)
    links = LinkBaseSerializer(many=True, read_only=True)

    class Meta(GroupBaseSerializer.Meta):
        fields = GroupBaseSerializer.Meta.fields + ('links', 'owner')


class LinkWithNestedSerializer(LinkBaseSerializer):
    """
    Link serializer with nested group
    """
    # groups = GroupBaseSerializer(many=True)
    # (треба щоб коли вводжу то міг вводити лише id групи, а коли виводжу то виводило все)

    class Meta(LinkBaseSerializer.Meta):
        fields = LinkBaseSerializer.Meta.fields + ('groups', )
