from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)

from .forms import ActualizarEmpleadoForm
# Create your views here.

# Models
from .models import Empleado

class InicioView(TemplateView):
    ''' Vista que carga la pagina de Inicio '''
    template_name = 'inicio.html'

class ListarTodosEmpleados(ListView):
    template_name = 'personal/list_all.html'
    context_object_name = 'empleados'
    ''' Paginación de datos '''
    paginate_by = 4 

    ''' Ordenar '''
    ordering = 'id'

    def get_queryset(self):
        print('****************')
        palabra_clave = self.request.GET.get('kword', '')

        ''' consulta a la base de datos y filtro '''
        lista = Empleado.objects.filter(
            first_name__icontains = palabra_clave
        )
        print('========>', lista)
        return lista

class ListarTodosEmpleadosAdmin(ListView):
    model = Empleado
    template_name = 'personal/lista_empleados.html'
    context_object_name = 'empleados'
    ''' Paginación de datos '''
    paginate_by = 5

    ''' Ordenar '''
    ordering = 'first_name'

class ListarPorAreaEmpleados(ListView):
    """ Listar empleados por area """
    template_name = 'personal/empleados_por_area.html'

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

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        
        return context


class SuccessView(TemplateView):
    template_name = 'personal/success.html'


class EmpleadoCreateView(CreateView):
    template_name = 'personal/agregar_empleado.html'
    model = Empleado
    # campos que necesita para rellenar
    fields = [
        'first_name',
        'second_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'hoja_vida',
        'image'
    ]
    # la url a la que va redireccionar una vez enviado los datos
    success_url = reverse_lazy('persona_app:correcto')

    def form_valid(self, form):
        #logica del proces
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.second_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    template_name = 'personal/actualizar_empleado.html'
    model = Empleado
    #form_class = ActualizarEmpleadoForm
    # campos para actualizar
    fields = [
        'first_name',
        'second_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'hoja_vida',
    ]
    # la url a la que va redireccionar una vez enviado los datos
    success_url = reverse_lazy('persona_app:empleados_admin')

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     print('*******Metodo post*******')
    #     print(request.POST)
    #     print(request.POST['last_name'])
    #     return super().post(request, *args, **kwargs)
    
    # def form_valid(self, form):
    #     #logica del proces
    #     print('*******Metodo form valid*******')
    #     return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    template_name = 'personal/borrar_empleado.html'
    model = Empleado
    success_url = reverse_lazy('persona_app:empleados_admin')