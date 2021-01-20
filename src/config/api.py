from ninja import NinjaAPI
from apps.users.api import router as users_router

api = NinjaAPI(
    docs_url='/docs/',
    title='Помощьник гражданина API',
    version='0.1.2',
    description='''API для сервиса "помощьник гражданина". На данный момент сервис
    позволяет собирать информацию о проблемах в городе.'''
)

api.add_router("/api/v1/user/", users_router)
