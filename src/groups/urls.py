from django.urls import path, include
from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from .views import GroupViewSet, LinkViewSet, CustomUserViewSet


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass

router = NestedDefaultRouter()

groups_links = router.register('groups', GroupViewSet)
groups_links.register(
    'links',
    LinkViewSet,
    basename="groups_links",  # for reverse(), has to be unique across API
    parents_query_lookups=['group']  # for filter. Link.object.filter(group={value from url})
)
router.register('links', LinkViewSet, 'links')
router.register('users', CustomUserViewSet, 'users')

urlpatterns = router.urls  # API endpoints
