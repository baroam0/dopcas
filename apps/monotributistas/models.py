
from django.db import models

class Monotributista(models.Model):
    apellido = models.CharField(max_length=70, blank=False, null=False)
    nombre = models.CharField(max_length=70, blank=False, null=False)
    numerodocumento = models.CharField(max_length=9, blank=False, null=False)
    cuit = models.CharField(max_length=11, blank=False, null=False)
    domicilio = models.CharField(max_length=11, blank=False, null=False)

    def __str__(self):
        return self.apellido + ', ' + self.nombre

    class Meta:
        verbose_name_plural = "Monotributistas"


# Create your models here.
