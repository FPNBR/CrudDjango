from unicodedata import name
from django.urls import path
from .views import viewHome, viewAutor, viewAutorAdd, viewAutorEdit, viewAutorDelete, viewEditora, viewEditoraAdd, viewEditoraEdit, viewEditoraDelete


urlpatterns = [
    path('home/', viewHome, name='home'),
    path('autor/', viewAutor, name='autor'),
    path('autor/add/', viewAutorAdd, name='autor_add'),
    path('autor/edit/<int:autor_pk>', viewAutorEdit, name='autor_edit'),
    path('autor/delete/<int:autor_pk>', viewAutorDelete, name='autor_delete'),
    path('editora/', viewEditora, name='editora'),
    path('editora/add/', viewEditoraAdd, name='editora_add'),
    path('editora/edit/<int:editora_pk>', viewEditoraEdit, name='editora_edit'),
    path('editora/delete/<int:editora_pk>', viewEditoraDelete, name='editora_delete')
]