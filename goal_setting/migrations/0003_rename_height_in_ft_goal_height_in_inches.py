# Generated by Django 4.2.11 on 2024-04-25 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal_setting', '0002_goal_last_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goal',
            old_name='height_in_ft',
            new_name='height_in_inches',
        ),
    ]
