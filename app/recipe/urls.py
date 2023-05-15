"""
URL mapping for the recipe app
"""
from django.urls import include, path
from recipe.views import RecipeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("recipes", RecipeViewSet)

app_name = "recipe"

urlpatterns = [
    path("", include(router.urls)),
]
