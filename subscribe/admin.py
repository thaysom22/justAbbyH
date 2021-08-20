from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    fields = ('user', 'country', 'city',
              'start_date', 'stripe_pid',)
    list_display = ('user', 'country', 'city',
                    'start_date', 'stripe_pid',)
    readonly_fields = ('start_date', 'stripe_pid',)
    ordering = ('-start_date',)


# CREDIT[16]
# subclass default UserAdmin to display attached subscription
class UserAdminCustom(UserAdmin):
    list_display = ('email', 'first_name', 'last_name',
                    'subscription', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')


admin.site.unregister(User)
admin.site.register(User, UserAdminCustom)
admin.site.register(Subscription, SubscriptionAdmin)
