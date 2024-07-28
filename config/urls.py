from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path(
        "woody/",
        include(
            [
                path(
                    "schema/",
                    SpectacularAPIView.as_view(api_version="v1"),
                    name="schema",
                ),
                path(
                    "",
                    SpectacularSwaggerView.as_view(url_name="schema"),
                    name="swagger-ui",
                ),
                path(
                    "redoc/",
                    SpectacularRedocView.as_view(url_name="schema"),
                    name="redoc",
                ),
                path("admin/", admin.site.urls),
                path("", include(("core.interfaces.apis.urls", "api"))),
            ]
        ),
        name="woody",
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

