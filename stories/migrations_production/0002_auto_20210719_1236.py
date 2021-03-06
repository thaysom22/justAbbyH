# Generated by Django 3.2.4 on 2021-07-19 16:36

import custom_storages
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='image',
            field=models.ImageField(
                blank=True, storage=custom_storages.PublicFileStorage(), upload_to='story_images/'),
        ),
        migrations.AlterField(
            model_name='story',
            name='pdf',
            field=models.FileField(
                storage=custom_storages.PrivateFileStorage(), upload_to='story_pdfs/'),
        ),
    ]
