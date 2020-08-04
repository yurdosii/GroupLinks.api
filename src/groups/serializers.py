"""
API serializers
"""

from rest_framework import serializers
from groups.models import CustomUser, Group, Link


class CustomUserBaseSerializer(serializers.ModelSerializer):
    """
    CustomUser base serializer
    """
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'date_joined')


class CustomUserAdminSerializer(CustomUserBaseSerializer):
    """
    CustomUser serializer for admin
    """
    class Meta(CustomUserBaseSerializer.Meta):
        fields = '__all__'


class GroupBaseSerializer(serializers.ModelSerializer):
    """
    Group base serializer
    """
    owner = CustomUserBaseSerializer(read_only=True)
    linksLength = serializers.IntegerField(source='links.count')

    class Meta:
        model = Group
        fields = ('id', 'name', 'description', 'created', 'owner', 'linksLength')


class LinkBaseSerializer(serializers.ModelSerializer):
    """
    Link base serializer (for nesting in Group)
    """
    isDone = serializers.BooleanField(source='is_done')

    class Meta:
        model = Link
        fields = ('id', 'url', 'description', 'isDone', 'added', 'group')


class GroupWithNestedSerializer(GroupBaseSerializer):
    """
    Group serializer with nested links
    """
    links = LinkBaseSerializer(many=True, read_only=True)

    class Meta(GroupBaseSerializer.Meta):
        fields = GroupBaseSerializer.Meta.fields + ('links', )
