# Generated by Django 3.2.4 on 2021-08-18 11:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20210816_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='reading_time_mins',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(600000), django.core.validators.MinValueValidator(1)]),
        ),
    ]