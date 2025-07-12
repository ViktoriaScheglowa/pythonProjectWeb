from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Класс создания модели пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Phone', help_text="Введите номер телефона")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Avatar')
    country = models.CharField(max_length=35, blank=True, null=True)
    token = models.CharField(max_length=100, blank=True, null=True, verbose_name="Token")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
