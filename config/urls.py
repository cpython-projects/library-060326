"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import (SpectacularAPIView,
                                   SpectacularSwaggerView,
                                    SpectacularRedocView)

from apps.library.views.logout import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/name-examples/', include('apps.library.urls.urls_name_examples')),
    path('api/v1/germanlibrary/', include('apps.library.urls.urls_normal')),

    # path('api/v1/obtain-library_auth-token/', obtain_auth_token, name='obtain_auth_token'),
    # path('api/v1/logout/', LogoutView.as_view(), name='logout'),

    path('api/v1/users/', include('apps.users.urls')),

    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger_ui'),
    path('api/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('api/v1/auth/', include('apps.library_auth.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
