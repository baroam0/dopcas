
from django import forms

from .models import ContratoCooperativa
from apps.obras.models import Obra
from apps.complementos.models import UnidadTiempo
from apps.cooperativas.models import Contratista 


class ContratoCooperativaForm(forms.ModelForm):
    descripcion = forms.CharField(label="Descripcion", required=True)
    contratista = forms.ModelChoiceField(
        queryset=Contratista.objects.filter(cooperativa=True).order_by("descripcion"),
        label="Cooperativa",
        )
    fecha_inicio = forms.DateField(label="Fecha Inicio", required=True)
    fecha_fin = forms.DateField(label="Fecha Fin", required=True)
    montomensual = forms.DecimalField(label="Monto Mensual")

    def __init__(self, *args, **kwargs):
        super(ContratoCooperativaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ContratoCooperativa
        fields = ['descripcion' , 'contratista', 'fecha_inicio',
            'fecha_fin', 'montomensual']
