from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone_number = models.CharField(max_length=35, verbose_name='телефона', blank=True, null=True,
                                    help_text='введите номер телефона')
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', blank=True, null=True, )
    country = models.CharField(max_length=100, verbose_name='страна')
    token = models.CharField(max_length=100, verbose_name='token', blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
