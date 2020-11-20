from django.db import models


class Mes(models.Model):
    descripcion = models.CharField(max_length=20,null=False, blank=False, unique=True)

    def __str__(self):
        return self.descripcion.upper()
    
    class Meta:
        verbose_name_plural = "Meses"


class UnidadTiempo(models.Model):
    descripcion = models.CharField(max_length=20,null=False, blank=False, unique=True)

    def __str__(self):
        return self.descripcion.upper()
    
    class Meta:
        verbose_name_plural = "Unidades de Tiempo"

# Create your models here.
