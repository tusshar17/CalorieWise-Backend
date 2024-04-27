from django.contrib import admin
from .models import Goal


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Goal._meta.fields if field.name != "id"]
