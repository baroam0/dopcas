
from django.db import models

from apps.complementos.models import UnidadTiempo
from apps.cooperativas.models import Contratista
from apps.obras.models import Obra


class ContratoObra(models.Model):
    obra = models.ForeignKey(Obra, null=True, blank=True, on_delete=models.CASCADE)
    contratista = models.ForeignKey(Contratista, on_delete=models.CASCADE)
    poliza = models.CharField(max_length=250, null=True, blank=True)
    numeropoliza = models.CharField(max_length=250, null=True, blank=True)
    plazo = models.IntegerField(null=True, blank=True)
    unidadtiempo = models.ForeignKey(UnidadTiempo, on_delete=models.CASCADE, default=1)
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    inicio_pliegogeneral = models.IntegerField(null=True, blank=True)
    fin_pliegogeneral = models.IntegerField(null=True, blank=True)

    inicio_pliegoparticular = models.IntegerField(null=True, blank=True)
    fin_pliegoparticular = models.IntegerField(null=True, blank=True)

    inicio_pliegotecnico = models.IntegerField(null=True, blank=True)
    fin_pliegotecnico = models.IntegerField(null=True, blank=True)

    plano = models.IntegerField(null=True, blank=True)
    oferta = models.IntegerField(null=True, blank=True)
    analisiprecio = models.IntegerField(null=True, blank=True)
    plantrabajo = models.IntegerField(null=True, blank=True)
    curvainversion = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.obra.descripcion) + " - " + str(self.contratista.descripcion)
        
    class Meta:
        verbose_name_plural = "Contratos de Obras"


# Create your models here.
