"""
API ViewSets
"""

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404
from .models import Group, Link
from .serializers import GroupWithNestedSerializer, LinkWithNestedSerializer


# custom ViewSet for this 2 identical ViewSet
class GroupViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
    Group viewset
    """
    queryset = Group.objects.all()
    permission_classes = [
        permissions.AllowAny
        # permissions.IsAuthenticated
    ]
    serializer_class = GroupWithNestedSerializer

    @action(detail=False) # "/groups/recent_groups"
    def recent_groups(self, request):
        """
        TODO Delete this method later
        """
        # import pdb; pdb.set_trace()
        recent_groups = Group.objects.all().order_by('-name')

        serializer = self.get_serializer(recent_groups, many=True)
        return Response(serializer.data)

    # def list(self, request):
    #     # import pdb; pdb.set_trace()

    #     # if not request.user.is_admin:  # is_staff
    #     #     self.queryset = self.queryset.filter(owner=request.user)

    #     # serializer = GroupWithNestedSerializer(self.queryset, many=True)
    #     # return Response(serializer.data)
    #     return super(GroupViewSet, self).list(self, request)

    # def retrieve(self, request, pk=None):
    #     # ! питання - в двох з super(), тут без
    #     # group = self.get_object()

    #     # if group.owner != request.user and not group.owner.is_admin:
    #     #     response_data = {"detail": "You aren't the group owner."}
    #     #     return Response(response_data, status=status.HTTP_403_FORBIDDEN)

    #     # serializer = GroupWithNestedSerializer(group)
    #     # return Response(serializer.data)

    #     return super(GroupViewSet, self).retrieve(self, request, pk=pk)

    # def update(self, request, *args, **kwargs):
    #     # group = self.get_object()

    #     # if group.owner != request.user and not group.owner.is_admin:
    #     #     response_data = {"detail": "Forbidden to update. You aren't the group owner"}
    #     #     return Response(response_data, status=status.HTTP_403_FORBIDDEN)

    #     return super(GroupViewSet, self).update(self, request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     # group = self.get_object()

    #         # if group.owner != request.user and not group.owner.is_admin:
    #     #     response_data = {"detail": "Forbidden to delete. You aren't the group owner"}
    #     #     return Response(response_data, status=status.HTTP_403_FORBIDDEN)

    #     return super(GroupViewSet, self).destroy(self, request, *args, **kwargs)


    # def get_permissions(self): / get_serializer_class(self)
    #     if self.action in ['retrieve', '']:
    #         return [IsAuthenticated()]
    #     else:
    #         return super(self, UserViewSet).get_permissions()


class LinkViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
    Link viewset
    """
    queryset = Link.objects.all()
    permission_classes = [
        permissions.AllowAny
        # permissions.IsAuthenticated
    ]
    serializer_class = LinkWithNestedSerializer

    # same methods
