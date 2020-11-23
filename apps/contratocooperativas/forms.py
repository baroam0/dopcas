
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
    poliza = forms.CharField(label="Poliza")
    numeropoliza = forms.CharField(label="Numero Poliza")
    tareas = forms.CharField(label="Tareas")
    plazo = forms.IntegerField(label="Plazo")
    unidadtiempo = forms.ModelChoiceField(
        label="Unidad de Tiempo",
        queryset=UnidadTiempo.objects.all().order_by("descripcion"),
        required=True
    )
    montomensual = forms.DecimalField(label="Monto Mensual")

    def __init__(self, *args, **kwargs):
        super(ContratoCooperativaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ContratoCooperativa
        fields = ['descripcion' , 'contratista', 'poliza',
            'numeropoliza', 'tareas', 'plazo', 'unidadtiempo',
            'montomensual' ]
