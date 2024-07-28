from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

# API Documentation URLs
api_documentation_patterns = [
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
]

# Admin URLs
admin_patterns = [
    path("admin/", admin.site.urls),
]

# Core API URLs
core_api_patterns = [
    path("", include(("core.interfaces.endpoints.urls", "api"), namespace="core")),
]

urlpatterns = [
    path("woody/", include(api_documentation_patterns)),
    path("woody/", include(core_api_patterns)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:  # Admin should be available only in DEBUG mode
    urlpatterns += admin_patterns
