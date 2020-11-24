
from django import forms

from .models import ContratoObra
from apps.obras.models import Obra
from apps.complementos.models import UnidadTiempo
from apps.cooperativas.models import Contratista 


class ContratoObraForm(forms.ModelForm):
    obra = forms.ModelChoiceField(
        queryset=Obra.objects.all(),
        label="Obra",
        required=True
    )
    contratista = forms.ModelChoiceField(
        queryset=Contratista.objects.filter(cooperativa=False).order_by("descripcion"),
        label="Cooperativa",
    )
    poliza = forms.CharField(label="Poliza")
    numeropoliza = forms.CharField(label="Numero Poliza")
    montopoliza = forms.DecimalField(label="Monto Poliza")
    plazo = forms.IntegerField(label="Plazo")
    unidadtiempo = forms.ModelChoiceField(
        label="Unidad de Tiempo",
        queryset=UnidadTiempo.objects.all().order_by("descripcion"),
        required=True
    )
    monto = forms.DecimalField(label="Monto")

    inicio_pliegogeneral = forms.IntegerField(label="Inicio Pliego General", required=True)
    fin_pliegogeneral = forms.IntegerField(label="Fin Pliego General", required=True)

    inicio_pliegoparticular = forms.IntegerField(label="Inicio Pliego Particular", required=True)
    fin_pliegoparticular = forms.IntegerField(label="Fin Pliego Particular", required=True)

    inicio_pliegotecnico = forms.IntegerField(label="Inicio Pliego Tecnico", required=True)
    fin_pliegotecnico = forms.IntegerField(label="Fin Pliego Tecnico", required=True)

    plano = forms.IntegerField(label="Foja de Plano", required=True)
    oferta = forms.IntegerField(label="Foja de Oferta", required=True)
    analisiprecio = forms.IntegerField(label="Foja Analisis de Precio", required=True)
    plantrabajo = forms.IntegerField(label="Foja Plan de Trabajo", required=True)
    curvainversion = forms.IntegerField(label="Foja Curva de Inversion", required=True)
    foja_decreto = forms.IntegerField(label="Foja de Decreto", required=True)

    def __init__(self, *args, **kwargs):
        super(ContratoObraForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ContratoObra
        fields = ['obra', 'contratista', 'poliza',
            'numeropoliza', 'montopoliza', 'plazo', 'unidadtiempo',
            'monto', 'inicio_pliegogeneral', 'fin_pliegogeneral',
            'inicio_pliegoparticular', 'fin_pliegoparticular',
            'inicio_pliegotecnico', 'fin_pliegotecnico',
            'plano', 'oferta', 'analisiprecio', 'plantrabajo',
            'curvainversion', 'foja_decreto']






    
    

    