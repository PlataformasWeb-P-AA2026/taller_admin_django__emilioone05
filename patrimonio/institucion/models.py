from django.db import models
import datetime
# Create your models here.
class Museo(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    ciudad = models.CharField(max_length=45)
    anio_fundacion = models.IntegerField()
    
    def costo_total_produccion(self):
        guias = self.museomain.all()
        return sum(
            exh.costo_produccion
            for guia in guias
            for exh in guia.guiaexh.all()
        )
        
        
    def experiencia_guia(self):
        guias = list(self.museomain.all())
        if not guias:
            return "Sin guías"
        max_exp = 0
        for guia in guias:
            if guia.anios_experiencia_guia > max_exp:
                max_exp = guia.anios_experiencia_guia
        nombres = []
        for guia in guias:
            if guia.anios_experiencia_guia == max_exp:
                nombres.append(guia.nombre_completo_guia)
                
        return ", ".join(nombres)
    
    
    def __str__(self): 
        return f"Nombre: {self.nombre} "
    
class GuiaMuseo(models.Model):
    nombre_completo_guia = models.CharField(max_length=60)
    anios_experiencia_guia = models.IntegerField()
    idiomas_hablados = models.CharField(max_length=100)
    museo = models.ForeignKey(
        Museo,
        related_name='museomain',
        on_delete= models.CASCADE
    )
    def __str__(self): 
        return f"NombreGuia: {self.nombre_completo_guia} | Experiencia: {self.anios_experiencia_guia} | IdiomasManejados: {self.idiomas_hablados} | Museo: {self.museo}"
    
class Exibicion(models.Model):
    titulo_exhibicion = models.CharField(max_length=50)
    meses_duracion = models.IntegerField()
    costo_produccion = models.DecimalField(max_digits=10, decimal_places=2)
    tematica = models.CharField(max_length=50)
    guia = models.ForeignKey(
        GuiaMuseo,
        related_name='guiaexh',
        on_delete=models.CASCADE
    )
    def __str__(self): 
        return f"Titulo: {self.titulo_exhibicion} | DuracionMeses: {self.meses_duracion} | CostoProduccion: {self.costo_produccion} | Tematica: {self.tematica} | GuiaEncargado {self.guia}"
    