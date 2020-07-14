
from django.db import models


class Material(models.Model):
    descripcion = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name_plural = "Materiales"


# Create your models here.
