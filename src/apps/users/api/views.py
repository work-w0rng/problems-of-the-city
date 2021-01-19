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
def create(request, user: schemas.User):

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
