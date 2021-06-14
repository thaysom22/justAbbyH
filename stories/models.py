from django.db import models

from math import floor


class Story(models.Model):
    """
    Stores data for story instances
    """
    
    FICTION = 'Fiction'
    NON_FICTION = 'Non-fiction'
    UNKNOWN = 'Unknown'

    GENRE_CHOICES = [
        (FICTION, 'Fiction'),
        (NON_FICTION, 'Non-fiction'),
        (None, 'Select a genre'),
    ]  # genre widget is select box
    
    genre = models.CharField(
        max_length=50,
        choices=GENRE_CHOICES,
        blank=True,
        default=None,
    )  # NOT USED IN CURRENT VERSION

    title = models.CharField(max_length=254)
    publish_date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='story_images/', blank=True)
    pdf = models.FileField(upload_to='story_pdfs/')
    featured = models.BooleanField(blank=True, null=False, default=False)  # NOT USED IN CURRENT VERSION
    reading_time_mins = models.PositiveIntegerField(default=0)  # NOT USED IN CURRENT VERSION

    def __str__(self):
        return f"id:{self.id} title:{self.title}"

    def display_reading_time(self):
        """ 
        Returns human readable string representing
        reading time of story in hours and mins
        """
        hours = floor(self.reading_time_mins / 60)
        mins = self.reading_time_mins % 60
        if hours:
            return f"{hours} hours and {mins} mins"
        elif mins:
            return f"{mins} mins"
        else:
            return "Unknown"
