from django.urls import path

from . import views
from .webhooks import webhook_listener


urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('create-inactive-user/', views.create_inactive_user, name='create_inactive_user'),
    path('confirm-deletion-of-inactive-user/', views.confirm_deletion_of_inactive_user, name='confirm_deletion_of_inactive_user'),
    path('subscription-created/', views.subscription_created, name='subscription_created'),
    path('webhooks/', webhook_listener, name='webhook_listener'),
    path('activate/<uidb64>/<token>/', views.activate_user, name='activate_user'),
]
