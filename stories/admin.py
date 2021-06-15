from django.contrib import admin

from .models import Story


class StoryAdmin(admin.ModelAdmin):
    fields = ('title', 'publish_date', 'genre',
              'description', 'reading_time_mins',
              'reading_time_string',
              'featured', 'image', 'pdf',)

    list_display = ('title', 'publish_date', 'genre',
                    'reading_time_mins',
                    'featured', 'image', 'pdf',)
    
    readonly_fields = ('publish_date', 'reading_time_string',)
    ordering = ('-publish_date',)


admin.site.register(Story, StoryAdmin)