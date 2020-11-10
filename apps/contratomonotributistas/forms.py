
from django import forms

from apps.monotributistas.models import Monotributista
from .models import ContratoMonotributista, TipoContrato


class ContratoMonotributistaForm(forms.ModelForm):
    tipocontrato = forms.ModelChoiceField(
        queryset=TipoContrato.objects.all(),
        label = 'Tipo Contrato',
        required=True,
    )
    monotributista = forms.ModelChoiceField(
        queryset=Monotributista.objects.all(),
        label = 'Monotributista',
        required=True,
    )
    fecha_inicio = forms.DateField(label="Fecha Inicio", required=True)
    fecha_fin = forms.DateField(label="Fecha Fin", required=True)
    monto_mensual = forms.DecimalField(label='Monto Mensual')

    def __init__(self, *args, **kwargs):
        super(ContratoMonotributistaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ContratoMonotributista
        fields = ['tipocontrato', 'monotributista', 'fecha_inicio',
            'fecha_fin', 'monto_mensual']

