"""
API ViewSets
"""

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
# from django.shortcuts import get_object_or_404
from .models import Group, Link
from .serializers import GroupWithNestedSerializer, LinkWithNestedSerializer


class GroupViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
    Group viewset
    """
    queryset = Group.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
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

    def list(self, request, *args, **kwargs):
        if not request.user.is_admin:  # is_staff
            self.queryset = self.queryset.filter(owner=request.user)

        return super(GroupViewSet, self).list(self, request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        instance = self.get_object()

        if not request.user.is_admin and instance.owner != request.user:
            response_data = {"detail": "You aren't the owner."}
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)

        return super(GroupViewSet, self).retrieve(self, request, pk=pk)

    #! can't test without token authentication
    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if not request.user.is_admin and instance.owner != request.user:
            response_data = {"detail": "Forbidden to update. You aren't the owner"}
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)

        return super(GroupViewSet, self).update(self, request, *args, **kwargs)

    #! can't test without token authentication
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if not request.user.is_admin and instance.owner != request.user:
            response_data = {"detail": "Forbidden to delete. You aren't the owner"}
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)

        return super(GroupViewSet, self).destroy(self, request, *args, **kwargs)


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
        # permissions.AllowAny
        permissions.IsAuthenticated
    ]
    serializer_class = LinkWithNestedSerializer

