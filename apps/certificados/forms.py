
from django import forms

from .models import Monotributista


class CertificadoForm(forms.ModelForm):

    obra = forms.ModelChoiceField(
        queryset=obra.objects.all(),
        label="Obra")

    contratista = forms.ModelChoiceField(
        queryset=Contratista.objects.all(),
        label="Contratista")

    numero = forms.CharField(
        label="Numero",
        required=False)

    monto = forms.DecimalField(label="Monto", required=True)

    expediente = forms.CharField(label="Expediente", required=True)


    def __init__(self, *args, **kwargs):
        super(MonotributistaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Monotributista
        fields = ['obra', 'contratista', 'numero', 'monto', 'expediente']


