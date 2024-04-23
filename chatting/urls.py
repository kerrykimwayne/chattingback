"""
URL configuration for chatting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from chatte.views import utilisateurserialiser,utilisateurserialiser_detail,readandcreatmessage
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listandcreat/',utilisateurserialiser.as_view(),name='listandcreate'),
    path('listandcreats/<int:pk>',utilisateurserialiser_detail.as_view(),name='listandcreatedetail'),
    path('veriftoken/',readandcreatmessage.as_view(),name='message'),
    path('api/token/obtain/',obtain_auth_token,name='obtaintoken'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='refreshtoken'),
    path('api/token/verify/',TokenVerifyView.as_view(),name='verifytoken'),
]
