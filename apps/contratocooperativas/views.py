
from django.shortcuts import render

from .models import ContratoObra, TipoContrato



def detallecontratocontratista(request, pk):
    consulta = ContratoObra.objects.get(pk=pk)
    
    return render(request, "contratosobras/contrato_cooperativa.html", {})
   

# Create your views here.
