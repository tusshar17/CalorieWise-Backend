# Generated by Django 4.2.11 on 2024-04-19 02:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meal_logs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MealLogs',
            new_name='MealLog',
        ),
    ]
