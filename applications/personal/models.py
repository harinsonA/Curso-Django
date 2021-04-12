from django.db import models

from applications.departamento.models import Departamento

from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Lista de Habilidades' # darle un nombre en plural
        ordering = ['habilidad'] # Para ordenar

    def __str__(self):
        return str(self.id) +' - '+ self.habilidad

# Create your models here.
class Empleado(models.Model):
    """ Modelo para tabla de empleados """
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'DESARROLLADOR'),
    )
    first_name = models.CharField('Primer Nombre', max_length=50)
    second_name = models.CharField('Segundo Nombre', max_length=50)
    last_name = models.CharField('Apellidos', max_length=90)
    job = models.CharField('Rol', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    image =  models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Mi Personal'
        verbose_name_plural = 'Areas de Recursos Humanos' # darle un nombre en plural
        ordering = ['first_name'] # Para ordenar
       


    def __str__(self):
        return str(self.id) +' - '+ self.first_name + ' ' + self.last_name 
