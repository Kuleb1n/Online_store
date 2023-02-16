from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    email = models.EmailField(_("Email address"), unique=True)
    user_photo = models.ImageField('User photo', upload_to='users/%Y/%m/%d/', blank=True)
    is_the_email_confirmed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class EmailConfirmation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    code = models.UUIDField('Code', unique=True)
    created = models.DateTimeField('Created', auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailConfirmation object for {self.user.email}'
