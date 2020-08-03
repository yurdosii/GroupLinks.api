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
    class Meta:
        model = Group
        fields = ('id', 'name', 'description', 'created')


class LinkBaseSerializer(serializers.ModelSerializer):
    """
    Link base serializer (for nesting in Group)
    """
    isDone = serializers.BooleanField(source='is_done')

    class Meta:
        model = Link
        fields = ('id', 'url', 'description', 'isDone', 'added')


class GroupWithNestedSerializer(GroupBaseSerializer):
    """
    Group serializer with nested links
    """
    owner = CustomUserBaseSerializer(read_only=True)
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
