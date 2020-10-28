
from django.shortcuts import render

from .models import ContratoMonotributista


def detallecontrato(request):
    resultado = ContratoMonotributista.objects.get(pk=1)
    return render(request, "contratomonotributistas/detallecontrato.html", {"resultado": resultado})


# Create your views here.
