from rest_framework.authentication import BaseAuthentication
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class Custom(BaseAuthentication):
    def authenticate(self, request):
        username=request.data.get('username')
        password=request.data.get('password')
        User=get_user_model()
        user=User.objects.get(username=username)
        if user.check_password(password):
            return (user,None)
        else:
            return None
        