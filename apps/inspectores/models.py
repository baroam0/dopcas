
from django.db import models


class Inspector(models.Model):
    apellido = models.CharField(max_length=100, null=False, blank=False)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    telelfono = models.CharField(max_length=15)

    def __str__(self):
        return self.apellido + ", " + self.nombre

    class Meta:
        verbose_name_plural = "Inspectores"


# Create your models here.
