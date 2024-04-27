from django.contrib import admin
from .models import WeightRecord


@admin.register(WeightRecord)
class weightRecordAdmin(admin.ModelAdmin):
    list_display = ["user", "weight", "created_at"]
