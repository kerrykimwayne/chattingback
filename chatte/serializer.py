from .models import Utilisateurs,Message
from rest_framework import serializers
from django.conf import settings
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model= Utilisateurs
        fields=['pk','nom','prenom','username','email','password','confirmpassword']
        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model= Message
        fields=['pk','message','expediteur','recepteur']
  
   

           
    