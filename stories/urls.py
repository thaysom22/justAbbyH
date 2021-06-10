from django.urls import path

from . import views


urlpatterns = [
    path('', views.stories, name='stories'),
    path('<int:story_id>/', views.story_detail, name='story_detail'),
    path('add/', views.add_story, name='add_story'),
    path('edit/<int:story_id>/', views.edit_story, name='edit_story'),
    path('delete/<int:story_id>/', views.delete_story, name='delete_story'),
]