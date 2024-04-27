from django.urls import path
from .views import (
    WeightListCreate,
    GetEarliestWeight,
    GetLatestWeight,
    GetDaysAgoWeight,
)


urlpatterns = [
    path("", WeightListCreate.as_view()),
    path("get_current/", GetLatestWeight.as_view()),
    path("get_first/", GetEarliestWeight.as_view()),
    path("get_from_last_x_days/<int:days>", GetDaysAgoWeight.as_view()),
]
