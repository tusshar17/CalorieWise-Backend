from django.urls import path, include
from goal_setting import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", views.GoalModelViewSet, basename="Goals")

urlpatterns = [
    path("", include(router.urls)),
]

#
