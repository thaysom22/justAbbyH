from django.urls import path

from . import views


urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('create-inactive-user/', views.create_inactive_user, name='create_inactive_user'),
    path('delete-inactive-user/', views.delete_inactive_user, name='delete_inactive_user'),
    path('subscription-created/', views.subscription_created, name='subscription_created'),
]
