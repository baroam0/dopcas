
from django import forms

from .models import Contratista


class ContratistaForm(forms.ModelForm):
    descripcion = forms.CharField(label="Descripcion", required=False)
    cuit = forms.CharField(label="CUIT", required=False)
    domicilio = forms.CharField(label="Domicilio", required=False)
    titular = forms.CharField(label="Titular", required=False)

    def __init__(self, *args, **kwargs):
        super(ContratistaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Contratista
        fields = ['descripcion', 'cuit', 'domicilio', 'titular']

