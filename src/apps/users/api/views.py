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
    '/register/', 
    response={
        200: schemas.Token, 
        401: schemas.Error, 
        402: List[schemas.Error]
    }
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
    '/login/',
    response={
        200: schemas.Token,
        401: schemas.Error
    }
)
def login(request, user: schemas.Login):
    user_ = models.User.objects.filter(email=user.email).first()
    if not user_ or not user_.check_password(user.password):
        return 401, {'message': 'Введите правильную почту или пароль'}
    
    return 200, {'token': user_.token}


@router.put(
    '/reset_password/',
    response={
        200: schemas.Token,
        401: schemas.Error,
        402: List[schemas.Error]
    }
)
def reset_password(request, user: schemas.ResetPassword):
    user_ = models.User.objects.filter(email=user.email).first()
    if not user_ or not user_.check_password(user.old_password):
        return 401, {'message': 'Введите правильную почту или пароль'}
    if user.old_password == user.new_password:
        return 401, {'message': 'Новый пароль не должен совпадать со старым'}
    
    user_.password = user.new_password
    try:
        user_.save()
    except ValidationError as error:
        return 402, [{'message': message} for message in error.messages]

    return 200, {'token': user_.token}
