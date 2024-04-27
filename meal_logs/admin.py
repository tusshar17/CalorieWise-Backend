from django.contrib import admin
from .models import MealLog


@admin.register(MealLog)
class MealLogsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MealLog._meta.fields if field.name != "id"]
