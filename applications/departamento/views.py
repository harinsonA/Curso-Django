from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView, ListView

#importar los modelos
from applications.personal.models import Empleado
from .models import Departamento

from .forms import NuevoDepartamentoForm
# Create your views here.

class ListarDepartamentos(ListView):
    template_name = 'departamento/lista_departamento.html'
    context_object_name = 'departamentos'
    paginate_by = 4
    ordering = 'name'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        ''' consulta a la base de datos y filtro '''
        lista = Departamento.objects.filter(
            name__icontains = palabra_clave
        )
        return lista

class DetalleDepartamento(DetailView):
    model = Departamento
    template_name = 'departamento/detalle_departamento.html'

class NuevoDepartamento(FormView):
    template_name = 'departamento/nuevo_departamento.html'
    form_class = NuevoDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print("******** Estamos en el form valid **********")

        _departamento = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['nombre_corto_departamento'],
        )
        _departamento.save()

        primer_nombre = form.cleaned_data['primer_nombre']
        segundo_nombre = form.cleaned_data['segundo_nombre']
        apellidos = form.cleaned_data['apellidos']

        Empleado.objects.create(
            first_name=primer_nombre,
            second_name=segundo_nombre,
            last_name=apellidos,
            job='1',
            departamento=_departamento,
        )

        return super(NuevoDepartamento, self).form_valid(form)