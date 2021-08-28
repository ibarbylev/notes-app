from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_profile_or_list_of_notes, name='index'),
    path('add/', views.create_note_view, name='note_create'),
    path('edit/<int:pk>/', views.NoteUpdateView.as_view(), name='note_update'),
    path('delete/<int:pk>/', views.NoteDeleteView.as_view(), name='note_delete'),
    path('details/<int:pk>/', views.NoteDetailView.as_view(), name='note_detail'),
]
