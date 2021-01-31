from . import router, schemas
from .. import models
from django.core.exceptions import ValidationError
from apps.api.authorizations import AuthWithEmailAndPassword, AuthWithToken
import logging


logging.basicConfig(level=logging.DEBUG)


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

    Пароль, содержащийся в поле **password** должен соответствовать требованиям безопастности:

        - иметь минимум 8 символов;
        - состоять не только из цифр.
    """
    if models.User.objects.filter(email=user.email):
        return 400, {'codes': ['email_already_use']}

    user = models.User(
        full_name=user.full_name,
        address=user.address,
        email=user.email,
        password=user.password,
    )

    try:
        user.save()
    except ValidationError as error:
        return 400, {'codes': [e for e in error]}

    return 200, {'token': user.token}


@router.get(
    '/',
    response=schemas.SignIn,
    auth=AuthWithEmailAndPassword(),
    tags=['Работа с пользователем'],
    summary='Авторизация',
    operation_id='login'
)
def login(request):
    return 200, {
        'token': request.auth.token,
        'full_name': request.auth.full_name,
        'address': request.auth.address
    }


@router.put(
    '/',
    response={
        200: schemas.Token,
        400: schemas.Error
    },
    auth=AuthWithToken(),
    tags=['Работа с пользователем'],
    summary='Смена пароля',
    operation_id='reset_password'
)
def reset_password(request, reset_password: schemas.ResetPassword):
    user = request.auth

    if not user.check_password(reset_password.old_password):
        return 400, {'codes': ['invalid_password']}

    user.password = reset_password.new_password
    try:
        user.save()
    except ValidationError as error:
        return 400, {'codes': [e for e in error]}

    return 200, {'token': user.token}
