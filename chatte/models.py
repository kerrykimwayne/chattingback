from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Utilisateurs(AbstractUser):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    confirmpassword=models.CharField(max_length=50)
    
class Message(models.Model):
    message=models.TextField()
    expediteur=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='expediteur')
    recepteur=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='recepteur')
    date_envoie=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message