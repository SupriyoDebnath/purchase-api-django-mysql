"""purchase_mysql_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic.base import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('pm-mysql/v1/admin/', admin.site.urls),
    path('', RedirectView.as_view(url='pm-mysql/v1/admin/', permanent=False), name='index'),

    path('pm-mysql/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('pm-mysql/v1/schema/doc/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('pm-mysql/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('pm-mysql/v1/', include('customer.routers')),
    path('pm-mysql/v1/', include('product.routers')),
    path('pm-mysql/v1/', include('invoice.routers')),
]
