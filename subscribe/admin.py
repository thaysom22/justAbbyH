from django.contrib import admin

from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    fields = ('user', 'country', 'city',
              'start_date', 'stripe_pid',)
              
    list_display = ('user', 'country', 'city',
                    'start_date', 'stripe_pid',)
    
    readonly_fields = ('start_date', 'stripe_pid',)
    ordering = ('-start_date',)


admin.site.register(Subscription, SubscriptionAdmin)