
from django.db import models

from apps.complementos.models import UnidadTiempo
from apps.cooperativas.models import Contratista
from apps.obras.models import Obra


class ContratoCooperativa(models.Model):
    descripcion = models.CharField(max_length=1000, null=True, blank=True)
    contratista = models.ForeignKey(Contratista, on_delete=models.CASCADE)
    poliza = models.CharField(max_length=250, null=True, blank=True)
    numeropoliza = models.CharField(max_length=250, null=True, blank=True)
    tareas = models.CharField(max_length=250, null=True, blank=True)
    plazo = models.IntegerField(null=True, blank=True)
    montomensual = models.DecimalField(max_digits=10, decimal_places=2, default=1)

    def __str__(self):
        return str(self.descripcion) + " - " + str(self.contratista.descripcion)
        
    class Meta:
        verbose_name_plural = "Contratos de Cooperativas"


# Create your models here.
