"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:

    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)





urlpatterns = [
    path('admin/',admin.site.urls),
    path('api/token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/library/',include('library.urls')),
    path('api/account/',include('account.urls')),
]
