
from django import forms

from .models import ContratoObra, TipoContrato
from apps.obras.models import Obra
from apps.cooperativas.models import Contratista 


class ContratoObraForm(forms.ModelForm):
    obra = forms.ModelChoiceField(queryset=Obra.objects.all(), label="Obra")
    contratista = forms.ModelChoiceField(
        queryset=Contratista.objects.all().order_by("descripcion"),
        label="Contratista")

    tipocontrato = forms.ModelChoiceField(
        queryset=TipoContrato.objects.all().order_by("descripcion"),
        label="Tipo Contrato", required=True)

    poliza = forms.CharField(label="Nombre Aseguradora", required=False)
    numeropoliza = forms.CharField(label="Numero de Poliza", required=False)
    tareas = forms.CharField(label="Tareas a Realizar", required=False)

    def __init__(self, *args, **kwargs):
        super(ContratoObraForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ContratoObra
        fields = ['obra', 'contratista', 'tipocontrato', 'poliza', 'numeropoliza', 'tareas']

