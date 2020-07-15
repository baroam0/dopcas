

from django import forms

from .models import Obra


class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ["descripcion", "expediente"]