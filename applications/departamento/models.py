from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, unique=True)
    shor_name = models.CharField('Nombre Corto', max_length=20, blank=True)
    anulate = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la empresa' # darle un nombre en plural
        ordering = ['name'] # Para ordenar
        unique_together = ('name', 'shor_name') # Para que no se repitan o vuelvan a crear cambos con el mismo nombre

    def __str__(self):
        return str(self.id) +' - '+ self.name +' - '+ str(self.anulate)
