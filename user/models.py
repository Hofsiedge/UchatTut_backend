# user/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.postgres.fields import ArrayField
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

    is_tutor    = models.BooleanField(default=False)
    form        = models.PositiveIntegerField(null=True)
    related     = models.ManyToManyField('self', symmetrical=True)
    subjects    = ArrayField(models.CharField(max_length=50), null=True, blank=True)

    phone_number = models.BigIntegerField(default=0)
    address     = models.CharField(max_length=100, default='')

    photo       = models.ImageField(null=True, blank=True)

    fcm_token   = models.CharField(max_length=200, null=True)


    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

