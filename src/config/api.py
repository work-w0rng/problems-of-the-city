from ninja import NinjaAPI
from apps.users.api import router as users_router

api = NinjaAPI(
    docs_url='/docs/'
)

api.add_router("/api/v1/user/", users_router)
