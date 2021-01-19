from . import router, schemas
from .. import models


@router.post(
    '/register/', 
    response={
        200: schemas.Token,
    }
)
def create(request, user: schemas.User):
    user = models.User.objects.create(
        full_name=user.full_name,
        address=user.address,
        email=user.email,
        password=user.password,
    )
    return 200, {'token': user.token}
