from django.shortcuts import render

from .models import Utilisateurs,Message
from rest_framework import generics,authentication
from rest_framework.response import Response
from .serializer import UserSerializer,MessageSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
# Create your views here.
user=get_user_model()
class utilisateurserialiser(generics.ListCreateAPIView):
    queryset=user.objects.all()
    serializer_class=UserSerializer
    filter_backends=(DjangoFilterBackend,SearchFilter)
    filterset_fields=('username','password')
    
    
class utilisateurserialiser_detail(generics.RetrieveAPIView):
    queryset=user.objects.all()
    serializer_class=UserSerializer
    authentication_classes=[authentication.TokenAuthentication]


class readandcreatmessage(generics.ListCreateAPIView):
     queryset=Message.objects.all()
     serializer_class=MessageSerializer
     filter_backends=(DjangoFilterBackend,SearchFilter)
     filterset_fields=['expediteur']


     