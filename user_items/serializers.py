from rest_framework import serializers
from .models import FoodItem, Recipe


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = "__all__"
        extra_kwargs = {"user": {"read_only": True}}


# -------------- Recipe ------------------------
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}, "user": {"read_only": True}}
