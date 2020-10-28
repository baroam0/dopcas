
from django.db import models

from apps.monotributistas.models import Monotributista
from apps.tiposcontratos.models import TipoContrato


class ContratoMonotributista(models.Model):
    tipocontrato = models.ForeignKey(TipoContrato, on_delete=models.CASCADE)
    monotributista = models.ForeignKey(Monotributista, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto_mensual = models.DecimalField(decimal_places=2, max_digits=15)

    def __str__(self):
        return str(self.monotributista)

    class Meta:
        verbose_name_plural = "Contratos Monotributistas"


 # Create your models here.
