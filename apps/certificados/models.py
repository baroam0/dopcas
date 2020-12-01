
from django.db import models

from apps.cooperativas.models import Contratista
from apps.obras.models import Obra


class Certificado(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    contratista = models.ForeignKey(Contratista, on_delete=models.CASCADE)
    numero = models.CharField(max_length=50, null=False, blank=False)
    monto = models.DecimalField(decimal_places=2, max_digits=10)
    expediente = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.obra) + " - " + str(self.contratista.descripcion)

    class Meta:
        verbose_name_plural = "Certificados"


# Create your models here.
