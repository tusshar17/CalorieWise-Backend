from django.urls import path, include
from .views import (
    WeightModelViewSet,
    GetEarliestWeight,
    GetLatestWeight,
    GetDaysAgoWeight,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("", WeightModelViewSet, basename="WeightModelViewSet")


urlpatterns = [
    path("/record/", include(router.urls)),
    path("/get_current/", GetLatestWeight.as_view()),
    path("/get_first/", GetEarliestWeight.as_view()),
    path("/get_from_last_x_days/<int:days>", GetDaysAgoWeight.as_view()),
]
