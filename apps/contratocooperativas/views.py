
from django.shortcuts import render, redirect

from .forms import ContratoCooperativaForm
from .models import ContratoCooperativa
from apps.complementos.models import Mes
from apps.tiposcontratos.models import TipoContrato
from lib.numeroatexto import numtxt, numerotxt
from lib.cuentames import totalmes


def detallecontratocontratista(request, pk):
    resultado = ContratoMonotributista.objects.get(pk=pk)
    tipocontrato = TipoContrato.objects.get(pk=int(resultado.tipocontrato.pk))
    plazo = totalmes(resultado.fecha_inicio, resultado.fecha_fin)
    montocontrato = plazo * resultado.monto_mensual
    letramontomensual = numtxt(resultado.monto_mensual)
    letramontocontrato = numtxt(montocontrato)
    letraplazo = numerotxt(int(plazo))
    
    if tipocontrato.descripcion == "Contrato Administrativo":
        return render(
            request,
            "tiposcontratos/contrato_administrativo.html",
            {
                "resultado": resultado,
                "plazo": plazo,
                "montocontrato": montocontrato,
                "letramontocontrato": letramontocontrato,
                "letramontomensual" : letramontomensual,
                "letraplazo": letraplazo
            }
        )

    if tipocontrato.descripcion == "Contrato Maquinista":
        return render(
            request,
            "tiposcontratos/contrato_maquinista.html",
            {
                "resultado": resultado,
                "plazo": plazo,
                "montocontrato": montocontrato,
                "letramontocontrato": letramontocontrato,
                "letramontomensual" : letramontomensual,
                "letraplazo": letraplazo
            }
        )
    
    if tipocontrato.descripcion == "Contrato Tecnico":
        return render(
            request,
            "tiposcontratos/contrato_tecnico.html",
            {
                "resultado": resultado,
                "plazo": plazo,
                "montocontrato": montocontrato,
                "letramontocontrato": letramontocontrato,
                "letramontomensual" : letramontomensual,
                "letraplazo": letraplazo
            }
        )

    
def listadocontratocooperativa(request):
    if "txtbuscar" in request.GET:
        parametro = request.GET.get("txtbuscar")
        resultados = ContratoCooperativa.objects.filter(obra__descripcion__contains=parametro)
    else:
        resultados = ContratoCooperativa.objects.all()
    return render(
        request,
        "contratoscooperativas/lista_contratocooperativa.html",
        {
            "resultados": resultados
        })


def nuevocontratocooperativa(request):
    if request.POST:
        form = ContratoCooperativaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listadocontratomonotributista')
        else:
            return render(request, 'contratosobras/editar_contratoobra.html', {"form": form})
    else:
        form = ContratoCooperativaForm()
        return render(request, 'contratosobras/editar_contratoobra.html', {"form": form})


def editarcontratocooperativa(request, pk):
    consulta = ContratoMonotributista.objects.get(pk=pk)
    if request.POST:
        form = ContratoObraForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('/listadocontratomonotributista')
        else:
            return render(
                request,
                'contratomonotributistas/editar_contratomonotributista.html',
                {"form": form}
            )
    else:
        form = ContratoObraForm(instance=consulta)
        return render(request, 'contratomonotributistas/editar_contratomonotributista.html', {"form": form})


# Create your views here.

