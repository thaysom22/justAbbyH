from django.contrib import admin

from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    fields = ('user', 'first_name', 'last_name',
              'email', 'country', 'city',
              'start_date',)
    list_display = ('user', 'first_name', 'last_name',
                    'email', 'country', 'city',
                    'start_date',)
    
    readonly_fields = ('start_date',)
    ordering = ('-start_date',)


admin.site.register(Subscription, SubscriptionAdmin)