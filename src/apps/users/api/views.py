from django.http import response
from . import router, schemas
from .. import models
from django.core.exceptions import ValidationError
from typing import List


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


@router.post(
    '/login/',
    response={
        200: schemas.Token,
        401: schemas.Error
    }
)
def login(request, user: schemas.Login):
    user_ = models.User.objects.filter(email=user.email).first()
    if not user_:
        return 401, {'message': 'Введите правильную почту или пароль'}
    if not user_.check_password(user.password):
        return 401, {'message': 'Введите правильную почту или пароль'}
    
    return 200, {'token': user_.token}
