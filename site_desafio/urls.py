from unicodedata import name
from django.urls import path
from .views import viewHome, viewAutor, viewAutorAdd, viewAutorEdit, viewAutorDelete


urlpatterns = [
    path('home/', viewHome, name='home'),
    path('autor/add/', viewAutorAdd, name='autor_add'),
    path('autor/edit/<int:autor_pk>', viewAutorEdit, name='autor_edit'),
    path('autor/delete/<int:autor_pk>', viewAutorDelete, name='autor_delete'),
    path('autor/', viewAutor, name='autor')
]