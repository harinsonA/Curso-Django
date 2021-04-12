from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)

# Para personalizar el Admin de Recursos Humanos
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )
    # Para mostrar el nombre completo
    def full_name(self, obj):
        return f"{obj.first_name} {obj.second_name} {obj.last_name}"

    # Para busqueda
    search_fields = ('first_name',)

    # Para filtrar
    list_filter = (
        'departamento',
        'job',
    )
    # Filtro Horizontal
    filter_horizontal = ('habilidades',)


admin.site.register(Empleado, EmpleadoAdmin)