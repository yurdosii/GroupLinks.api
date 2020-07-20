"""
API ViewSets
"""

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Group, Link
from .serializers import GroupWithNestedSerializer, LinkWithNestedSerializer


class GroupViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
    Group viewset
    """
    queryset = Group.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GroupWithNestedSerializer

    # def create(self, request):
    #     import pdb; pdb.set_trace()

    # def update(self, request, pk=None):
    #     pass

    @action(detail=False) # "/groups/recent_groups"
    def recent_groups(self, request):
        """
        TODO Delete this method later
        """
        recent_groups = Group.objects.all().order_by('-name')

        serializer = self.get_serializer(recent_groups, many=True)
        return Response(serializer.data)


class LinkViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
    Link viewset
    """
    queryset = Link.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LinkWithNestedSerializer
