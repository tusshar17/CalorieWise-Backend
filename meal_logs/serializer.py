from rest_framework import serializers
from .models import MealLog
import random


def calculteFoodItemMacros(val, serving_size, qty_used):
    return (val / serving_size) * qty_used


def calculateTotalMacros(data):
    res = {
        "meals_macros": dict(),
        "day_calories": 0,
        "day_protein": 0,
        "day_carbs": 0,
        "day_fats": 0,
        "day_sugar": 0,
    }

    for meal in data["logs"]:
        print(meal)
        meal["meal_id"] = meal["meal_name"].split(" ")[0] + str(random.randint(10, 99))
        meal_macros = {
            "calories": 0,
            "protein_in_g": 0,
            "carbs_in_g": 0,
            "fats_in_g": 0,
            "sugar_in_g": 0,
        }
        for food_item in meal["food_items"]:
            serving_size = food_item["serving_size_in_g"]
            qty_used = food_item["qty_used_in_g"]

            for key in list(meal_macros.keys()):
                meal_macros[key] += calculteFoodItemMacros(
                    food_item[key], serving_size, qty_used
                )

        res["meals_macros"][meal["meal_name"]] = meal_macros

        for key_res, key_meal_macros in zip(list(res.keys())[1:], meal_macros.keys()):
            res[key_res] += meal_macros[key_meal_macros]

    return res


def setDayAndMealMacros(data):
    # count total day macros and each meal macros
    macros = calculateTotalMacros(data)
    print(macros)
    # set day macros
    for key in list(macros.keys())[1:]:
        data[key] = macros[key]
    # set meal macros
    count = 0
    for meal_name in macros["meals_macros"]:
        data["logs"][count]["meal_macros"] = macros["meals_macros"][meal_name]
        count += 1
    return data


class MealLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealLog
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "user": {"read_only": True},
            "day_calories": {"read_only": True},
            "day_protein": {"read_only": True},
            "day_carbs": {"read_only": True},
            "day_fats": {"read_only": True},
            "day_sugar": {"read_only": True},
        }

    def create(self, validated_data):
        validated_data = setDayAndMealMacros(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = setDayAndMealMacros(validated_data)
        return super().update(instance, validated_data)


class MacroSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = MealLog
        exclude = ["logs"]
