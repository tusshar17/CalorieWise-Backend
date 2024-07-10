from rest_framework import serializers
from .models import FoodItem, Recipe
from .util import CalculateRecipeMacros


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

    def create(self, validated_data):
        recipeMacros = CalculateRecipeMacros.calculateRecipeMacros(
            validated_data.get("recipe_items", None)
        )
        for key in recipeMacros:
            validated_data[key] = recipeMacros[key]
        print("creating recipe", validated_data)
        return super().create(validated_data)
