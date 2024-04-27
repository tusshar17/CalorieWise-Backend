from rest_framework import serializers
from goal_setting.models import Goal


def inches_to_cm(height_inches):
    height_cm = height_inches * 2.54
    return height_cm


def calculateGoal(data):
    if data["gender"].lower() == "m":
        data["goal_sugar"] = 37.5
        bmr = (
            (10 * data["starting_weight_in_kg"])
            + (6.25 * inches_to_cm(data["height_in_inches"]))
            - (5 * data["age"])
            + 5
        )
    else:
        data["goal_sugar"] = 25
        bmr = (
            (10 * data["starting_weight_in_kg"])
            + (6.25 * inches_to_cm(data["height_in_inches"]))
            - (5 * data["age"])
            - 161
        )

    maintainance_calories = data["pal"] * bmr
    surplus_calories = data["weekly_goal"] * 1000
    data["goal_calories"] = maintainance_calories + surplus_calories
    data["goal_protein"] = (data["goal_calories"] * 0.3) / 4
    data["goal_carbs"] = (data["goal_calories"] * 0.4) / 4
    data["goal_fats"] = (data["goal_calories"] * 0.3) / 9
    return data


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
            "goal_calories": {"read_only": True},
            "goal_protein": {"read_only": True},
            "goal_carbs": {"read_only": True},
            "goal_fats": {"read_only": True},
            "goal_sugar": {"read_only": True},
        }

    def create(self, validated_data):
        validated_data = calculateGoal(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = calculateGoal(validated_data)
        return super().update(instance, validated_data)
