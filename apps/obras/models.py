from django.db import models

from apps.complementos.models import UnidadTiempo
from apps.cooperativas.models import Contratista


class TipoLicitacion(models.Model):
    descripcion = models.CharField(max_length=500, null=False, blank=False)
    
    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name_plural = "Tipos de Licitacion"


class Obra(models.Model):
    descripcion = models.CharField(max_length=500, null=False, blank=False)
    expediente = models.CharField(max_length=15, null=False, blank=False)
    decreto = models.CharField(max_length=15, null=False, blank=False)
    tipo_licitacion = models.ForeignKey(TipoLicitacion, on_delete=models.CASCADE)
    numero_licitacion = models.CharField(max_length=10, null=True, blank=True)
    plazo = models.IntegerField(null=True, blank=True)
    unidadtiempo = models.ForeignKey(UnidadTiempo, on_delete=models.CASCADE, null=True, blank=True)
    monto = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name_plural = "Obras"


class Adjudicacion(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    adjudicatario = models.ForeignKey(Contratista, on_delete=models.CASCADE)
    montoadjudicacion = models.DecimalField(decimal_places=2, max_digits=10)
    
    def __str__(self):
        return str(self.obra.descripcion) + " - " + str(self.adjudicatario)

    class Meta:
        verbose_name_plural = "Adjudicaciones"


# Create your models here.
