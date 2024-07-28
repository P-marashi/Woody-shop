# core/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.interfaces.category.views import CategoryViewSet

# Initialize the router
router = DefaultRouter()

# Register the CategoryViewSet
router.register(r'categories', CategoryViewSet, basename='category')

# Include the router URLs in the urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
