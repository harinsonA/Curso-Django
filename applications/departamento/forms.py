from django import forms

class NuevoDepartamentoForm(forms.Form):
    primer_nombre = forms.CharField(max_length=25)
    segundo_nombre = forms.CharField(max_length=25)
    apellidos = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    nombre_corto_departamento = forms.CharField(max_length=20)