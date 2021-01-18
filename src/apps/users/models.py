from django.db import models


class User(models.Model):
    full_name = models.CharField('ФИО', max_length=255)
    address = models.CharField('Адрес проживания', max_length=255)
    login = models.CharField('Логин', max_length=255, unique=True)
    email = models.EmailField('Почта', unique=True)
    date_joined = models.DateTimeField('Дата регистрации', auto_now_add=True)
    password = models.CharField('Хэш пароля', max_length=128)
    token = models.CharField('Токен', max_length=10)
