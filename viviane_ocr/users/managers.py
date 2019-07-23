from django.contrib.auth.models import BaseUserManager
from django.db.models import Q
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, name, password=None, **kwargs):
        if not email:
            raise ValueError('Por favor, insira um endereço de email válido.')

        user = self.model(
            email=self.normalize_email(email),
            name=name
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, name, password, **kwargs):
        user = self.create_user(email, name, password, **kwargs)

        user.is_superuser = True
        user.save()

        return user
