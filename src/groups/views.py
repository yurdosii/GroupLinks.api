"""
API ViewSets
"""

from rest_framework import viewsets, permissions, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CustomUser, Group, Link
from .serializers import (
    GroupWithNestedSerializer,
    LinkWithNestedSerializer,
    CustomUserAdminSerializer,
)


# pylint: disable=no-member
# pylint: disable=too-many-ancestors
class GroupViewSet(viewsets.ModelViewSet):
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

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        if not request.user.is_staff:  # is_staff
            self.queryset = self.queryset.filter(owner=request.user)

        return super().list(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        instance = self.get_object()

        if not request.user.is_staff and instance.owner != request.user:
            response_data = {"detail": "You aren't the owner."}
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)

        return super().retrieve(request, pk=pk)

    #! can't test without token authentication
    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if not request.user.is_staff and instance.owner != request.user:
            response_data = {"detail": "Forbidden to update. You aren't the owner"}
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)

        return super().update(request, *args, **kwargs)

    #! can't test without token authentication
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if not request.user.is_staff and instance.owner != request.user:
            response_data = {"detail": "Forbidden to delete. You aren't the owner"}
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)

        return super().destroy(request, *args, **kwargs)


    # def get_permissions(self): / get_serializer_class(self)
    #     if self.action in ['retrieve', '']:
    #         return [IsAuthenticated()]
    #     else:
    #         return super(self, UserViewSet).get_permissions()


class LinkViewSet(viewsets.ModelViewSet):
    """
    Link viewset
    """
    queryset = Link.objects.all()
    permission_classes = [
        # permissions.AllowAny
        permissions.IsAuthenticated
    ]
    serializer_class = LinkWithNestedSerializer

    def list(self, request, *args, **kwargs):
        if not request.user.is_staff:  # is_staff
            self.queryset = self.queryset.filter(groups__owner=request.user)

        return super().list(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        instance = self.get_object()

        if not request.user.is_staff and instance.groups.first().owner != request.user:
            response_data = {"detail": "You aren't the owner."}
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)

        return super().retrieve(request, pk=pk)

    #! can't test without token authentication
    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if not request.user.is_staff and instance.groups.first().owner != request.user:
            response_data = {"detail": "Forbidden to update. You aren't the owner"}
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)

        return super().update(request, *args, **kwargs)

    #! can't test without token authentication
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if not request.user.is_staff and instance.groups.first().owner != request.user:
            response_data = {"detail": "Forbidden to delete. You aren't the owner"}
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)

        return super().destroy(request, *args, **kwargs)


class CustomUserViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """
    CustomUser viewset
    Provides `retrieve`, and `list` actions.
    Available only for admins
    """
    queryset = CustomUser.objects.all()
    permission_classes = [
        permissions.IsAdminUser
    ]
    serializer_class = CustomUserAdminSerializer
