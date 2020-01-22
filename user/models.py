# user/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email       = models.EmailField(_('email address'), unique=True)
    is_staff    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    name        = models.CharField(max_length=50)
    surname     = models.CharField(max_length=50, default='')

    phone_number = models.BigIntegerField(default=0)
    address     = models.CharField(max_length=100, default='')

    photo       = models.ImageField(null=True, blank=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def json_repr(self):
        return {
            "id":       self.id,
            "name":     self.name,
            "surname":  self.surname,
            "phone":    self.phone_number,
            "address":  self.address,
            "photo":    "placeholder",
        }
