from django.contrib import admin
from django.contrib.auth import get_user_model
User=get_user_model()
from .models import Utilisateurs,Message
# Register your models here.

admin.site.register(Utilisateurs)
admin.site.register(Message)