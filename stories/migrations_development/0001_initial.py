# Generated by Django 3.2.4 on 2021-07-19 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(blank=True, choices=[('Fiction', 'Fiction'), ('Non-fiction', 'Non-fiction'), ('Unknown', 'Unknown'), ('Other', 'Other')], max_length=100, null=True)),
                ('title', models.CharField(max_length=254)),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('description', models.TextField(blank=True, max_length=6000, null=True)),
                ('featured', models.BooleanField(blank=True, default=False)),
                ('reading_time_mins', models.PositiveIntegerField(blank=True, null=True)),
                ('reading_time_string', models.CharField(max_length=254, null=True)),
                ('image', models.ImageField(blank=True, upload_to='public/story_images/')),
                ('pdf', models.FileField(upload_to='private/story_pdfs/')),
            ],
            options={
                'verbose_name_plural': 'Stories',
            },
        ),
    ]