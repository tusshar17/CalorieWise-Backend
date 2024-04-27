from django.urls import include, path
from meal_logs import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("log", views.MealLogModelViewSet, basename="MealLogModelViewSet")

urlpatterns = [
    path("/", include(router.urls)),
    path(
        "/get_macro_summary/<int:days>",
        views.MacroSummary.as_view(),
        name="MacroSummary",
    ),
]
