# Generated by Django 4.2.11 on 2024-06-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_is_verified_alter_user_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp',
            field=models.IntegerField(blank=True, default=6969, null=True),
        ),
    ]
