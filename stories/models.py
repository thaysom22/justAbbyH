from django.db import models


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
        default=UNKNOWN,
    )  # NOT USED IN CURRENT VERSION

    title = models.CharField(max_length=254)
    publish_date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='story_images/', blank=True)
    pdf = models.FileField(upload_to='story_pdfs/')
    featured = models.BooleanField(blank=True, null=False, default=False)  # NOT USED IN CURRENT VERSION

    def __str__(self):
        return f"id:{self.id} title:{self.title}"
    