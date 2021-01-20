from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import (
    check_password, make_password, is_password_usable
)
from string import ascii_letters, digits
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from .services.validators import validate_full_name
from .services.utils import convert_full_name


class User(models.Model):
    full_name = models.CharField('ФИО', max_length=255)
    address = models.CharField('Адрес проживания', max_length=255, blank=True, null=True)
    email = models.EmailField('Почта', unique=True)
    date_joined = models.DateTimeField('Дата регистрации', auto_now_add=True)
    password = models.CharField('Хэш пароля', max_length=128)
    token = models.CharField('Токен', max_length=10, editable=False)

    def save(self, *args, **kwargs):
        if is_password_usable(self.password):
            validate_password(self.password)
            validate_email(self.email)
            validate_full_name(self.full_name)

            self.full_name = convert_full_name(self.full_name)
            self.password = make_password(self.password)
            self.token = get_random_string(
                length=10, 
                allowed_chars=ascii_letters+digits
            )
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Гражданин'
        verbose_name_plural = 'Граждане'
