
from django import forms

from .models import Monotributista


class MonotributistaForm(forms.ModelForm):
    apellido = forms.CharField(label="Apellido", required=True)
    nombre = forms.CharField(label="Nombre", required=False)
    numerodocumento = forms.CharField(label="Nro Documento", required=True)
    cuit = forms.CharField(label="CUIT", required=False)
    domicilio = forms.CharField(label="Domicilio", required=True)

    def __init__(self, *args, **kwargs):
        super(MonotributistaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Monotributista
        fields = ['apellido', 'nombre', 'numerodocumento', 'cuit', 'domicilio']

