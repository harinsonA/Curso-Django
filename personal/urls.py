from django.contrib import admin
from django.urls import path

from . import views

app_name = 'persona_app'

urlpatterns = [
    path(
        '', 
        views.InicioView.as_view(),
        name='inicio',
    ),
    path(
        'listar-todo-empleados/', 
        views.ListarTodosEmpleados.as_view(),
        name='todos_empleados',
    ),
    path(
        'listar-por-area/<shorname>/',
        views.ListarPorAreaEmpleados.as_view(),
        name='empleados_por_area'
    ),
    path(
        'listar-empleados-admin/',
        views.ListarTodosEmpleadosAdmin.as_view(),
        name='empleados_admin'
    ),
    path('buscar-empleado/', views.ListarEmpleadoPorKwargs.as_view()),
    path('listar-habilidades-empleado/<id>/', views.ListaHabilidadesEmpleado.as_view()),
    path(
        'ver-empleado/<pk>/', 
        views.EmpleadoDetailView.as_view(),
        name='detalle_empleado'
    ),
    path(
        'agregar-empleado/',
         views.EmpleadoCreateView.as_view(),
         name='agregar_empleado'
        ),
    path(
        'success/', 
        views.SuccessView.as_view(), 
        name='correcto'
    ),
    path(
        'actualizar-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(), 
        name='actualizar_empleado'
    ),
    path(
        'borrar-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(), 
        name='borrar_empleado'
    ),

]
