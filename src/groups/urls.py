from django.urls import path, include
from rest_framework import routers
from .views import GroupViewSet, LinkViewSet


router = routers.DefaultRouter()
router.register('groups', GroupViewSet, 'groups')
router.register('links', LinkViewSet, 'links')

urlpatterns = router.urls  # API endpoints
