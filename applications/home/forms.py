#Importar primero paquete de django para los forms
from django import forms

#Importar modelo de datos (** Utilizamos el punto para hacer referencia al novel de archivo donde estamos posicionados entre las carpetas **)
from .models import Prueba

#code
#Modelo de clase de formulario
class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )

        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingresar Titulo',
                }
            ) 
        }

    def clean_cantidad(self):
        # Forma para capturar el valor del html
        cantidad = self.cleaned_data['cantidad']

        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')
            
        return cantidad
        