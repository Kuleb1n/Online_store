from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    email = models.EmailField(_("Email address"), unique=True)
    user_photo = models.ImageField('User photo', upload_to='users/%Y/%m/%d/', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
