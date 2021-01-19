from . import router, schemas
from .. import models


@router.post(
    '/register/', 
    response={
        200: schemas.Token, 
        401: schemas.Error,
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

    return 200, {'token': user.token}
