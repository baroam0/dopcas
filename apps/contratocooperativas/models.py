
from django.db import models

from apps.complementos.models import UnidadTiempo
from apps.cooperativas.models import Contratista
from apps.obras.models import Obra


class ContratoCooperativa(models.Model):
    descripcion = models.CharField(max_length=1000, null=True, blank=True)
    contratista = models.ForeignKey(Contratista, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    montomensual = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    cumplimentado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.descripcion) + " - " + str(self.contratista.descripcion)
        
    class Meta:
        verbose_name_plural = "Contratos de Cooperativas"


# Create your models here.
