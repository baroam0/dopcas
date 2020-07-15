from django.db import models


class Obra(models.Model):
    descripcion = models.CharField(max_length=100, unique=True)
    expediente = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name_plural = "Obras"


# Create your models here.
