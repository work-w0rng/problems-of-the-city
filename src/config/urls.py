from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from apps.api import api


admin.site.site_header = 'Помощьник гражданина'



urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("", api.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
