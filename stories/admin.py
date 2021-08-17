from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Story


class StoryAdmin(admin.ModelAdmin):
    fields = ('title', 'publish_date', 'genre',
              'description', 'reading_time_mins',
              'reading_time_string',
              'featured', 'image', 'image_credit',
              'pdf',)

    # replace 'pdf' field by '_pdf_download' return in list display
    list_display = ('title', 'publish_date', 'genre',
                    'reading_time_mins',
                    'featured', 'image', 'image_credit', '_pdf_download',)
    
    readonly_fields = ('publish_date', 'reading_time_string',)
    
    ordering = ('-publish_date',)

    # CREDIT[10]
    def _pdf_download(self, obj):
        """ 
        download story view url which
        provides signed url access to
        s3 bucket from admin list display
        """
        url_string = reverse('download_story', args=[obj.id])
        return format_html(
            f"<a href='{url_string}' target='_blank'>{obj.pdf.name}</a>")


admin.site.register(Story, StoryAdmin)
