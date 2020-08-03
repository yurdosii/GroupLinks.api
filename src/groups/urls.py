from django.urls import path, include
from rest_framework import routers
from .views import GroupViewSet, LinkViewSet, CustomUserViewSet


router = routers.DefaultRouter()
router.register('groups', GroupViewSet, 'groups')
router.register('links', LinkViewSet, 'links')
router.register('users', CustomUserViewSet, 'users')

urlpatterns = router.urls  # API endpoints
