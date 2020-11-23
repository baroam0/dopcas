
from django import forms

from .models import Contratista


class ContratistaForm(forms.ModelForm):
    descripcion = forms.CharField(label="Descripcion", required=False)
    cuit = forms.CharField(label="CUIT", required=False)
    domicilio = forms.CharField(label="Domicilio", required=False)
    titular = forms.CharField(label="Titular", required=False)
    doctitular = forms.CharField(label="Nro Doc Titular", required=False)
    representantetecnico = forms.CharField(label="Representante Tecnico", required=False)
    docrepresentantetecnico = forms.CharField(label="Nro Doc Rep Tecnico", required=False)
    cooperativa = forms.BooleanField(label="Es Cooperativa")

    def __init__(self, *args, **kwargs):
        super(ContratistaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Contratista
        fields = ['descripcion', 'cuit', 'domicilio', 'titular', 'doctitular',
            'representantetecnico', 'docrepresentantetecnico', 'cooperativa']

