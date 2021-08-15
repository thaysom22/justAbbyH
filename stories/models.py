from django.db import models
from django.conf import settings

from math import floor

USE_AWS = settings.USE_AWS
if USE_AWS:
    from custom_storages import PublicFileStorage, PrivateFileStorage


class Story(models.Model):
    """
    Stores data for story instances
    """

    class Meta:
        verbose_name_plural = "Stories"
    
    FICTION = 'Fiction'
    NON_FICTION = 'Non-fiction'
    UNKNOWN = 'Unknown'

    GENRE_CHOICES = [
        ('', 'Genre'),
        (FICTION, 'Fiction'),
        (NON_FICTION, 'Non-fiction'),
        (UNKNOWN, 'Unknown'),
    ]  # widget is select box
    
    genre = models.CharField(
        choices=GENRE_CHOICES,
        max_length=254,
        default='',
    )

    title = models.CharField(max_length=254, default='')
    publish_date = models.DateField(auto_now_add=True)
    description = models.TextField(default='')
    featured = models.BooleanField(default=False)
    reading_time_mins = models.PositiveIntegerField(null=True)
    reading_time_string = models.CharField(max_length=254, default='')
    image_credit = models.CharField(max_length=254, blank=True, default='')
    
    if USE_AWS:
        # specify custom s3 storages in production
        # for story image and pdf fields
        # CREDIT [4]
        image = models.ImageField(
            upload_to='story_images/',
            storage=PublicFileStorage(),
        )
        pdf = models.FileField(
            upload_to='story_pdfs/',
            storage=PrivateFileStorage(),
        )
    else:
        # use default local storage in development
        image = models.ImageField(upload_to='public/story_images/')
        pdf = models.FileField(upload_to='private/story_pdfs/')

    def __str__(self):
        if hasattr(self, 'id'):
            return f"Story <id:{self.id}>"
        else:
            return "Unsaved Story object"

    def save(self, *args, **kwargs):
        """ 
        Override inherited save() method to set
        reading_time_string attribute on class
        """
        if self.reading_time_mins:
            self.reading_time_string = self._generate_reading_time_string(
                self.reading_time_mins)

        super().save(*args, **kwargs)

    def _generate_reading_time_string(self, reading_time_mins):
        """
        Internal class method. Returns human readable
        string represention of reading time of story
        """
        hours = floor(reading_time_mins / 60)
        mins = reading_time_mins % 60
        if hours:
            return f"{hours} hours and {mins} mins"
        elif mins:
            return f"{mins} mins"
