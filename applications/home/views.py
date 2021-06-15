from django.shortcuts import render

# importar paquete de django que trabaja con vistas genericas
from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView
)

#import Models
from .models import Prueba

#import modelos Forms
from .forms import PruebaForm

# Create your views here.
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    template_name = 'home/lista.html'
    context_object_name = 'listaNumeros'  
    queryset = ['0', '10', '20', '30']

class ListarPrueba(ListView):
    template_name = 'home/listaprueba.html'
    model = Prueba
    context_object_name = 'lista'

class PruebaCreateView(CreateView):
    template_name = 'home/add.html'
    model = Prueba
    form_class = PruebaForm
    success_url = '/'