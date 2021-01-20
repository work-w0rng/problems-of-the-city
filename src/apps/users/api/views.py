from . import router, schemas
from .. import models
from django.core.exceptions import ValidationError
from typing import List
from ninja.security import HttpBasicAuth


class AuthWithEmailAndPassword(HttpBasicAuth):
    def authenticate(self, request, username, password):
        user = models.User.objects.filter(email=username).first()
        if user and user.check_password(password):
            return user


@router.post(
    '/', 
    response={
        200: schemas.Token, 
        400: schemas.Error,
    },
    tags=['Работа с пользователем'],
    summary='Регистрация',
    operation_id='register'
)
def register(request, user: schemas.Registration):
    """
    Регистрация нового пользователя пользователя.

    Поле **full_name** должно иметь формат *Фамилия Имя Отчество* или *Фамилия Имя*.

    Поле **address** не является обязательным.

    Поле **email** должно иметь корректный email.

    Пароль, содержащийся в поле **password** должен соотсветсвовать требованиям безопастности:

        - иметь минимум 8 символов;
        - состоять из цифр и букв.
    """
    errors = []
    if models.User.objects.filter(email=user.email):
        errors.append('email_already_use')

    user = models.User(
        full_name=user.full_name,
        address=user.address,
        email=user.email,
        password=user.password,
    )

    try:
        user.save()
    except ValidationError as error:
        for e in error:
            errors.append(e)

    if errors:
        return 400, {'codes': errors}

    return 200, {'token': user.token}


@router.get(
    '/',
    response=schemas.Token,
    auth=AuthWithEmailAndPassword(),
    tags=['Работа с пользователем'],
    summary='Авторизация',
    operation_id='login'
)
def login(request):
    return 200, {'token': request.auth.token}


@router.put(
    '/',
    response={
        200: schemas.Token,
        400: schemas.Error
    },
    auth=AuthWithEmailAndPassword(),
    tags=['Работа с пользователем'],
    summary='Смена пароля',
    operation_id='reset_password'
)
def reset_password(request, reset_password: schemas.ResetPassword):
    user = request.auth
    
    user.password = reset_password.new_password
    try:
        user.save()
    except ValidationError as error:
        return 400, {'codes': [e for e in error]}

    return 200, {'token': user.token}
