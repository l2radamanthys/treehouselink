from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from backend.settings import MEDIA_URL, MEDIA_ROOT, ENVIRONMENT


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("treelinks.urls")),
]

if ENVIRONMENT == "DEVELOPMENT":
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)