
from django import forms


from apps.cooperativas.models import Contratista
from apps.obras.models import Obra
from .models import Certificado


class CertificadoForm(forms.ModelForm):

    obra = forms.ModelChoiceField(
        queryset=Obra.objects.filter(concluida=False),
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
        super(CertificadoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Certificado
        fields = ['obra', 'contratista', 'numero', 'monto', 'expediente']

