from django.db import models
from account.models import User


class FoodItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    serving_size_in_g = models.FloatField(null=False, default=100)
    calories = models.FloatField(null=False)
    protein_in_g = models.FloatField(null=False)
    carbs_in_g = models.FloatField(null=False)
    fats_in_g = models.FloatField(null=False)
    sugar_in_g = models.FloatField(null=False)

    def __str__(self) -> str:
        return self.name + "-" + self.user.email


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    recipe_items = models.JSONField(blank=True)
    """
    recipe_items = [
        {
            id: ,
            is_custom: ,
            name: ,
            serving_size_in_g: ,
            calories: ,
            protein_in_g: ,
            carbs_in_g: ,
            fats_in_g: ,
            sugar_in_g: ,
            qty_used_in_g: ,
        }
    ]
    """
    total_calories = models.FloatField(blank=True)
    total_protein_in_g = models.FloatField(blank=True)
    total_carbs_in_g = models.FloatField(blank=True)
    total_fats_in_g = models.FloatField(blank=True)
    total_sugar_in_g = models.FloatField(blank=True)

    def __str__(self) -> str:
        return self.name + "-" + self.user.email
