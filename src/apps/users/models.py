from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import (
    check_password, make_password, is_password_usable
)
from string import ascii_letters, digits


class User(models.Model):
    full_name = models.CharField('ФИО', max_length=255)
    address = models.CharField('Адрес проживания', max_length=255, blank=True, null=True)
    email = models.EmailField('Почта', unique=True)
    date_joined = models.DateTimeField('Дата регистрации', auto_now_add=True)
    password = models.CharField('Хэш пароля', max_length=128)
    token = models.CharField('Токен', max_length=10, editable=False)

    def save(self, *args, **kwargs):
        if is_password_usable(self.password):
            self.password = make_password(self.password)
            self.token = get_random_string(
                length=10, 
                allowed_chars=ascii_letters+digits
            )
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
