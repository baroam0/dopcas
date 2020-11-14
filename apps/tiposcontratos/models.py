from django.db import models


class TipoContrato(models.Model):
    descripcion = models.CharField(max_length=100, unique=True)
    tareascontrato = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.descripcion.upper()
    
    class Meta:
        verbose_name_plural = "Tipos de Contratos"


# Create your models here.
