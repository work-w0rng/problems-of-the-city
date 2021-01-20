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
        401: schemas.Error, 
        402: List[schemas.Error]
    },
    tags=['Работа с пользователем'],
    summary='Регистрация',
    operation_id='register'
)
def register(request, user: schemas.Registration):
    if models.User.objects.filter(email=user.email):
        return 401, {'message': 'Данный email уже занят'}

    user = models.User(
        full_name=user.full_name,
        address=user.address,
        email=user.email,
        password=user.password,
    )

    try:
        user.save()
    except ValidationError as error:
        return 402, [{'message': message} for message in error.messages]

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
        402: List[schemas.Error]
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
        return 402, [{'message': message} for message in error.messages]

    return 200, {'token': user.token}
