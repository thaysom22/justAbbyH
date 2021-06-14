from django.db import models

from math import floor


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
    description = models.TextField(max_length=5000, blank=True, null=True)
    image = models.ImageField(upload_to='story_images/', blank=True)
    pdf = models.FileField(upload_to='story_pdfs/')
    featured = models.BooleanField(blank=True, null=False, default=False)  # NOT USED IN CURRENT VERSION
    reading_time_mins = models.PositiveIntegerField(blank=True, null=True)  # NOT USED IN CURRENT VERSION
    reading_time_string = models.CharField(max_length=254, blank=True, null=True)  # NOT USED IN CURRENT VERSION 

    def __str__(self):
        return f"id:{self.id} title:{self.title}"

    
    def save(self, *args, **kwargs):
        """ 
        Override inherited save() method to set
        reading_time_string attribute on class
        """
        self.reading_time_string = self._generate_reading_time_string(self.reading_time_mins)
        super().save(*args, **kwargs)


    def _generate_reading_time_string(self, total_mins):
        """ 
        Internal class method. Returns human readable 
        string represention of reading time of story 
        """
        if total_mins:
            hours = floor(total_mins / 60)
            mins = total_mins % 60
            if hours:
                return f"{hours} hours and {mins} mins"
            elif mins:
                return f"{mins} mins"
        else:
            return "Unknown"