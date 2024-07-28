from django.urls import path, include


urlpatterns = [
    path("v1/category/", include(("core.interfaces.category.urls", "category"), namespace="category")),
]
