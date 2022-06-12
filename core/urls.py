# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static

app_name = 'SSL'

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),             # UI Kits Html files
    path("api/", include('apps.api.urls')),
    path('', include("rest_framework.urls", namespace='rest_framework')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)