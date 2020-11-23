
from django import forms

from .models import Obra, TipoLicitacion
from apps.cooperativas.models import Contratista


class ObraForm(forms.ModelForm):
    descripcion = forms.CharField(label="Descripcion", required=True)
    expediente = forms.CharField(label="Expediente", required=True)
    decreto = forms.CharField(label="Decreto", required=True)
    tipo_licitacion = forms.ModelChoiceField(queryset=TipoLicitacion.objects.all(), label="Tipo Licitacion")
    numero_licitacion = forms.CharField(label="Nro Licitacion", required=False)
    monto = forms.DecimalField(label="Monto", required=True)

    def __init__(self, *args, **kwargs):
        super(ObraForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Obra
        fields = [
            'descripcion', 'expediente', 'decreto', 'tipo_licitacion',
            'numero_licitacion', 'monto']
