from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include("account.urls")),
    path("api/weight", include("weight_records.urls")),
    path("api/user-item", include("user_items.urls")),
    path("api/meal_logs", include("meal_logs.urls")),
    path("api/goal/", include("goal_setting.urls")),
]
