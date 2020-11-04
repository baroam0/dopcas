
from django.shortcuts import render

from .models import ContratoMonotributista
from lib.numeroatexto import numtxt
from lib.cuentames import totalmes

def detallecontrato(request, pk):
    resultado = ContratoMonotributista.objects.get(pk=pk)
    plazo = totalmes(resultado.fecha_inicio, resultado.fecha_fin)
    montocontrato = plazo * resultado.monto_mensual
    letramontocontrato = numtxt(montocontrato)
    return render(
        request,
        "contratomonotributistas/detallecontrato.html",
        {
            "resultado": resultado,
            "plazo": plazo,
            "montocontrato": montocontrato,
            "letramontocontrato": letramontocontrato
        })


# Create your views here.
