from django.contrib import admin
from .models import FoodItem, Recipe


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "name",
        "serving_size_in_g",
        "calories",
        "protein_in_g",
        "carbs_in_g",
        "fats_in_g",
        "sugar_in_g",
    ]


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Recipe._meta.fields if field.name != "id"]
