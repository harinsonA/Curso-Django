from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView
)
# Create your views here.

# Models
from .models import Empleado

class ListarTodosEmpleados(ListView):
    template_name = 'personal/list_all.html'

    ''' Paginación de datos '''
    paginate_by = 4 

    ''' Ordenar '''
    ordering = 'id'
    model = Empleado

class ListarPorAreaEmpleados(ListView):
    """ Listar empleados por area """
    template_name = 'personal/list_by_area.html'

    ''' metodo para filtrar '''
    def get_queryset(self):
        area = self.kwargs['shorname']

        ''' consulta a la base de datos y filtro '''
        lista = Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista

class ListarEmpleadoPorKwargs(ListView):
    ''' Listar Empleados por palabra clave '''
    template_name = 'personal/por_kwargs.html'
    context_object_name = 'empleados'

    ''' metodo para filtrar '''
    def get_queryset(self):
        print('****************')
        palabra_clave = self.request.GET.get('kword', '')

        ''' consulta a la base de datos y filtro '''
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        print('========>', lista)
        return lista

class ListaHabilidadesEmpleado(ListView):
    template_name = 'personal/lista_habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        id_empleado = self.kwargs['id']

        ''' consulta a la base de datos '''
        empleado = Empleado.objects.get(id=id_empleado)

        return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'personal/detalles_empleado.html'