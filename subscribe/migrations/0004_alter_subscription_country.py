# Generated by Django 3.2.4 on 2021-07-06 18:51

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0003_auto_20210706_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default='', max_length=2),
        ),
    ]