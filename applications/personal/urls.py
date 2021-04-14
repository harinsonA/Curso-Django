from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListarTodosEmpleados.as_view()),
    path('listar-por-area/<shorname>/', views.ListarPorAreaEmpleados.as_view()),
    path('buscar-empleado/', views.ListarEmpleadoPorKwargs.as_view()),
    path('listar-habilidades-empleado/<id>/', views.ListaHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view()),

]
