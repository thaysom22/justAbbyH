from django.urls import path

from . import views


urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('cache-inactive-user/', views.cache_inactive_user, name='cache_inactive_user'),
]
