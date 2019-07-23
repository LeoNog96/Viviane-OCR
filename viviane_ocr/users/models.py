from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from viviane_ocr.users.managers import UserManager
# from rest_framework.authtoken.models import Token

class User(AbstractBaseUser,PermissionsMixin):

    name = models.CharField(max_length = 200)

    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)

    phone = PhoneNumberField()

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_superuser

    class Meta:
        db_table = 'users'

    # @receiver(post_save, sender=User)
    # def create_token_api(sender, instance=None, created=False, **kwargs):
    #     if created:
    #         Token.objects.create(user=instance)

