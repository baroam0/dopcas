
from django.db import models

from apps.cooperativas.models import Contratista
from apps.obras.models import Obra


class TipoContrato(models.Model):
    descripcion = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.descripcion

    class Meta:
    verbose_name_plural = "Tipos de Contratos"


class ContratoObra(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    contratista = models.ForeignKey(Contratista, on_delete=models.CASCADE)
    tipocontrato = models.ForeignKey(TipoContrato, on_delete=models.CASCADE)
    poliza = models.CharField(max_length=250, null=True, blank=True)
    numeropoliza = models.CharField(max_length=250, null=True, blank=True)
    tareas = models.CharField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return str(self.obra.descripcion) + " - " + str(self.contratista.descripcion)
        
    class Meta:
        verbose_name_plural = "Contratos de Obra"

   

# Create your models here.
