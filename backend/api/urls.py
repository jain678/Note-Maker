from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('',views.getResponse,name='home'),
    path('notes/',views.NoteAPIView.as_view()),
    path('notes/<int:pk>',views.NoteAPIView.as_view()),

    # path('notes/create', views.createNote, name='create-note'),
    # path('notes/<str:pk>/update', views.updateNote, name='update-note'),
    # path('notes/<str:pk>/delete', views.deleteNote, name='delete-note'),
    # path('notes/<str:pk>',views.getNote, name='note'),
]