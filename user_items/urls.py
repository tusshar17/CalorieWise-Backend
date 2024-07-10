from django.urls import path, include
from user_items import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    "food-item", views.FoodItemModelViewSet, basename="FoodItemModelViewSet"
)

#
router.register("recipe", views.RecipeModelViewSet, basename="RecipeModelViewSet")

urlpatterns = [
    path("/", include(router.urls)),
    path("/search-food-item/<str:query>", views.searchFoodItem),
]
