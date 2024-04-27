# Generated by Django 4.2.11 on 2024-04-16 23:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('recipe_items', models.JSONField(blank=True)),
                ('total_calories', models.FloatField(blank=True)),
                ('total_protein_in_g', models.FloatField(blank=True)),
                ('total_carbs_in_g', models.FloatField(blank=True)),
                ('total_fats_in_g', models.FloatField(blank=True)),
                ('total_sugar_in_g', models.FloatField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
