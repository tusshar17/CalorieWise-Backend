# Generated by Django 4.2.11 on 2024-07-12 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight_records', '0002_rename_create_at_weightrecord_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weightrecord',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
