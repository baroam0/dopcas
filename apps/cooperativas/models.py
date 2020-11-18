from django.db import models


class Contratista(models.Model):
    descripcion = models.CharField(max_length=100, unique=True)
    cuit = models.CharField(max_length=11, unique=True)
    domicilio = models.CharField(max_length=150, unique=False)
    titular = models.CharField(max_length=100, unique=False)
    doctitular = models.CharField(max_length=100, unique=False)
    representantetecnico = models.CharField(max_length=100, unique=False)
    docrepresentantetecnico = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name_plural = "Contratistas"


class DocumentacionAdjunta(models.Model):
    contratista = models.ForeignKey(Contratista, on_delete=models.CASCADE)
    documentacion = models.FileField()

    def __str__(self):
        return self.contratista

    class Meta:
        verbose_name_plural = "Documentaciones Adjuntas"


# Create your models here.
