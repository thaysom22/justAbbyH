from django.urls import path

from . import views


urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('cache-inactive-user/', views.cache_inactive_user, name='cache_inactive_user'),
    path('activate-cached-user/', views.activate_cached_user, name='activate_cached_user'),
    path('delete-cached-user/', views.delete_cached_user, name='delete_cached_user'),
]
