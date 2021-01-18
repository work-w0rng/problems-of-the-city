from ninja import NinjaAPI
from apps.users.api import router as users_router

api = NinjaAPI(
    docs_url='/docs/'
)

api.add_router("/api/users/v1/", users_router)
