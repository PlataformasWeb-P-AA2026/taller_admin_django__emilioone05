from django.contrib import admin
from .models import Museo, GuiaMuseo, Exibicion
# Register your models here.


@admin.register(Exibicion)
class ExibicionAdmin(admin.ModelAdmin):
    list_display = ['titulo_exhibicion', 'meses_duracion', 'costo_produccion', 'tematica', 'guia']
    raw_id_fields = ['guia']

@admin.register(GuiaMuseo)
class GuiaMuseoAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo_guia', 'anios_experiencia_guia', 'idiomas_hablados', 'museo']

@admin.register(Museo)
class MuseoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ciudad', 'anio_fundacion', 'costo_total_produccion', 'experiencia_guia']