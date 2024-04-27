from django.db import models
from account.models import User


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    height_in_inches = models.IntegerField()
    starting_weight_in_kg = models.FloatField()
    pal = models.FloatField()  # physical activity level
    weekly_goal = models.FloatField()  # +/- 1  0.5 0.25
    goal_weight = models.FloatField()
    goal_calories = models.IntegerField()
    goal_protein = models.IntegerField()
    goal_carbs = models.IntegerField()
    goal_fats = models.IntegerField()
    goal_sugar = models.IntegerField()
    last_updated = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        self.starting_weight_in_kg = round(self.starting_weight_in_kg, 2)
        self.pal = round(self.pal, 2)
        self.weekly_goal = round(self.weekly_goal, 2)
        self.goal_weight = round(self.goal_weight, 2)
        super(Goal, self).save(*args, **kwargs)
