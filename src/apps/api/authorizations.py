from ninja.security import HttpBasicAuth, HttpBearer
from ..users.models import User


class AuthWithEmailAndPassword(HttpBasicAuth):
    def authenticate(self, request, username, password):
        user = User.objects.filter(email=username).first()
        if user and user.check_password(password):
            return user


class AuthWithToken(HttpBearer):
    def authenticate(self, request, token):
        user = User.objects.filter(token=token).first()
        if user:
            return user
