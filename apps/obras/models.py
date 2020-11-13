from django.db import models

from apps.cooperativas.models import Contratista


class Obra(models.Model):
    descripcion = models.CharFlield(max_length=500, null=False, blank=False)
    expediente = models.CharFlield(max_length=15, null=False, blank=False)
    decreto = models.CharFlield(max_length=15, null=False, blank=False)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name_plural = "Obras"


class Adjudicacion(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    adjudicatario = models.ForeignKey(Contratista, on_delete=models.CASCADE)
    montoadjudicacion = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        verbose_name_plural = "Adjudicaciones"


# Create your models here.
