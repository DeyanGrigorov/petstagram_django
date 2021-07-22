from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from petstagram_django.accounts.managers import PetstagramUserManager


class PetstagramUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = PetstagramUserManager()


class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to='profiles'
    )

    user = models.OneToOneField(
        PetstagramUser,
        on_delete=models.CASCADE,
        primary_key=True,
        blank=True,
    )


from .signals import *
