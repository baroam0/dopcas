
from django import forms

from .models import ContratoCooperativa
from apps.obras.models import Obra
from apps.cooperativas.models import Contratista 


class ContratoCooperativaForm(forms.ModelForm):
    descripcion = forms.CharField(label="Descripcion", required=True)
    contratista = forms.ModelChoiceField(
        queryset=Contratista.objects.all().order_by("descripcion"),
        label="",
        )
    poliza = forms.CharField(label="Poliza")
    numeropoliza = forms.CharField(label="Numero Poliza")
    tareas = forms.CharField(label="Tareas")
    plazo = forms.IntegerField(label="Plazo")
    montomensual = forms.DecimalField(label="Monto Mensual")

    def __init__(self, *args, **kwargs):
        super(ContratoCooperativaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ContratoCooperativa
        fields = ['descripcion' , 'contratista', 'poliza',
            'numeropoliza', 'tareas', 'plazo', 'montomensual'
        ]
