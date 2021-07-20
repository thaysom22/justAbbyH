from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.forms.widgets import ClearableFileInput

from .models import Story


class StoryAdmin(admin.ModelAdmin):
    fields = ('title', 'publish_date', 'genre',
              'description', 'reading_time_mins',
              'reading_time_string',
              'featured', 'image', 'pdf',)

    # replace 'pdf' field by 'pdf_download' field in list display
    list_display = ('title', 'publish_date', 'genre',
                    'reading_time_mins',
                    'featured', 'image', 'pdf_download',)
    
    readonly_fields = ('publish_date',)
    
    ordering = ('-publish_date',)

    # CREDIT[10]
    def pdf_download(self, obj):
        """ 
        Display url to download story view which
        generates signed s3 url
        """
        url_string = reverse('download_story', args=[obj.id])
        return format_html(f"<a href='{url_string}' target='_blank'>{obj.pdf.name}</a>")


admin.site.register(Story, StoryAdmin)
