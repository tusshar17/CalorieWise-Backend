from django.db import models
from account.models import User


class WeightRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField(null=False)
    created_at = models.DateTimeField()

    # def __str__(self):
    # return self.user.email + "-" + str(self.weight) + "-" + str(self.created_at)
