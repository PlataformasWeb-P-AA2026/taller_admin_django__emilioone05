from django.db import models
import datetime
# Create your models here.
class Museo(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    ciudad = models.CharField(max_length=45)
    anio_fundacion = models.IntegerField()
    
    def __str__(self): 
        return f"Nombre: {self.nombre} | Ciudad: {self.ciudad} | AñoFundacion: {self.anio_fundacion} |"
    
    
class GuiaMuseo(models.Model):
    nombre_completo_guia = models.CharField(max_length=60)
    anios_experiencia_guia = models.IntegerField()
    idiomas_hablados = models.CharField(max_length=30)
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
    costo_produccion = models.FloatField()
    tematica = models.CharField(max_length=50)
    guia = models.ForeignKey(
        GuiaMuseo,
        related_name='guiaexh',
        on_delete=models.CASCADE
    )
    def __str__(self): 
        return f"Titulo: {self.titulo_exhibicion} | DuracionMeses: {self.meses_duracion} | CostoProduccion: {self.costo_produccion} | Tematica: {self.tematica} | GuiaEncargado {self.guia}"
    