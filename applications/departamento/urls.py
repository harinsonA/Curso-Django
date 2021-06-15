from django.contrib import admin
from django.urls import path

from . import views

app_name = 'departamento_app'

urlpatterns = [
    path(
        'nuevo-departamento/',
        views.NuevoDepartamento.as_view(),
        name = 'nuevo_departamento'
    ),
    path(
        'lista-todos-departamentos/',
        views.ListarDepartamentos.as_view(),
        name = 'lista_todos_departamentos'
    ),
    path(
        'detalle-departamento/<pk>/',
        views.DetalleDepartamento.as_view(),
        name = 'detalle_departamento'
    ),
]
