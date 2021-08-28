from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_profile_or_list_of_notes, name='index'),
    path('add/', views.create_note_view, name='note_create'),
]
