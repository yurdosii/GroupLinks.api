"""grouplinks_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView


from groups.views_auth import handle_redirect, check_login


urlpatterns = [
    path('admin/', admin.site.urls),

    # path('api-auth/', include('rest_framework.urls')),
    path('check_login/', check_login),
    path('handle_redirect/', handle_redirect),
    path('social/', include('social_django.urls', namespace='social_auth')),

    path('auth/logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),

    path('api/v1/', include('groups.urls')),
]
