from django.db import models
from account.models import User
from django.utils import timezone


class MealLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    logs = models.JSONField(null=True, blank=True, default=None)
    """
    meals: [
        {
            meal_name:
            food_items:[
                {
                    id: ,
                    is_custom: ,
                    is_searched: ,
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
            calories:
            proein:
            carbs:
            sugar:
        }
    ]
    """
    day_calories = models.FloatField(null=True, blank=True, default=0)
    day_protein = models.FloatField(null=True, blank=True, default=0)
    day_carbs = models.FloatField(null=True, blank=True, default=0)
    day_fats = models.FloatField(null=True, blank=True, default=0)
    day_sugar = models.FloatField(null=True, blank=True, default=0)

    def __str__(self) -> str:
        return self.user.email + "-" + str(self.date)
