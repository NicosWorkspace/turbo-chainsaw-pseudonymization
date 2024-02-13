"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookstore/', include("bookstore.urls")),
    path('authors/', include("authormgmt.urls")),
    path('ehr/', include("ehr.urls")),
    path('accounts/login/', RedirectView.as_view(pattern_name='keycloak_login', permanent=False), name='account_login'),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls'))
]
