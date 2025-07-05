from django.urls import path
from .views import index, add_entry, edit_entry

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_entry, name='add_entry'),
    path('edit/<int:pk>/', edit_entry, name='edit_entry'),
]
