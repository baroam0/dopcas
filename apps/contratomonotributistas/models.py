
from django.db import models

from apps.monotributistas.models import Monotributista
from apps.tiposcontratos.models import TipoContrato


class ContratoMonotributista(models.Model):
    tipocontrato = models.ForeignKey(TipoContrato, on_delete=models.CASCADE)
    monotributista = models.ForeignKey(Monotributista, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=False, blank=False)
    monto_mensual = models.DecimalField(decimal_places=2, max_digits=15)
    decreto = models.CharField(max_length=15, null=True, blank=True)
    expediente = models.CharField(max_length=15, null=True, blank=True)
    cumplimentado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.monotributista)

    class Meta:
        verbose_name_plural = "Contratos Monotributistas"


 # Create your models here.
