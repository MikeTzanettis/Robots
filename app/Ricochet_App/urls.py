"""Ricochet_App URL Configuration

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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from testing.views import *
from testing import views


router = routers.DefaultRouter(trailing_slash=False)
router.register("games",GameViewSet,"games")
router.register("users",UserViewSet,"users")
router.register("squares",SquareViewSet,"squares")
router.register("turns",TurnViewSet,"turns")
router.register("bids",BidViewSet,"bids")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('<str:name>/',views.page)
    
]

urlpatterns+= staticfiles_urlpatterns()