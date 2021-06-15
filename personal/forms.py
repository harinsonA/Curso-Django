#Importar primero paquete de django para los forms
from django import forms

#Importar modelo de datos (** Utilizamos el punto para hacer referencia al novel de archivo donde estamos posicionados entre las carpetas **)
from .models import Empleado

#code
#Modelo de clase de formulario
class ActualizarEmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'second_name',
            'last_name',
            'job',
            'departamento',
            'habilidades',
            'hoja_vida',
        )

        widgets = {
            'first_name': forms.TextInput( attrs = { 'placeholder': 'Primer Nombre', 'class':'form-control'}), 
            'second_name': forms.TextInput( attrs = { 'placeholder': 'Segundo Nombre', 'class':'form-control'}), 
            'last_name': forms.TextInput( attrs = { 'placeholder': 'Apellidos','class':'form-control'}), 
            'job': forms.Select( attrs = { 'placeholder': 'Trabajo','class':'form-select'}), 
            'departamento': forms.Select( attrs = { 'placeholder': 'Departamento','class':'form-select'}), 
            'habilidades': forms.Select( attrs = { 'placeholder': 'Habilidades','class':'form-select'}), 
            'hoja_vida': forms.Textarea( attrs = { 'placeholder': 'Hoja de Vida','class':'form-control'}), 
        }