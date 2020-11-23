from django.db import models


class Contratista(models.Model):
    descripcion = models.CharField(max_length=100, unique=True)
    cuit = models.CharField(max_length=11, null=False, blank=False, unique=True)
    domicilio = models.CharField(max_length=150, unique=False)
    titular = models.CharField(max_length=100, null=False, blank=False, default="0")
    doctitular = models.CharField(max_length=100, null=False, blank=False, default="0")
    representantetecnico = models.CharField(max_length=100, null=True, blank=True)
    docrepresentantetecnico = models.CharField(max_length=100, null=True, blank=True)
    cooperativa = models.BooleanField(default=False)

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
