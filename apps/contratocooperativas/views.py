
import locale
from django.shortcuts import render, redirect


from .forms import ContratoCooperativaForm
from .models import ContratoCooperativa
from apps.complementos.models import Mes
from apps.tiposcontratos.models import TipoContrato
from lib.numeroatexto import numtxt, numerotxt
from lib.cuentames import totalmes


def detallecontratocooperativa(request, pk):
    locale.setlocale(locale.LC_ALL, '')

    resultado = ContratoCooperativa.objects.get(pk=pk)
    plazo = totalmes(resultado.fecha_inicio, resultado.fecha_fin)
    montocontrato = plazo * resultado.montomensual
    montocontrato = round(montocontrato,2)
    f_montocontrato = f'{montocontrato:n}'

    montomensual = round(resultado.montomensual,2)
    f_montomensual = f'{montomensual:n}'

    letramontomensual = numtxt(resultado.montomensual)
    letramontocontrato = numtxt(montocontrato)
    letraplazo = numerotxt(int(plazo))
    
    return render(
        request,
        "contratoscooperativas/contrato_cooperativa.html",
        {
            "resultado": resultado,
            "plazo": plazo,
            "montocontrato": f_montocontrato,
            "montomensual": f_montomensual,
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
            return redirect('/listadocontratocooperativa')
        else:
            return render(
                request,
                'contratoscooperativas/editar_contratocooperativa.html',
                {"form": form}
            )
    else:
        form = ContratoCooperativaForm()
        return render(
            request,
            'contratoscooperativas/editar_contratocooperativa.html',
            {"form": form}
        )


def editarcontratocooperativa(request, pk):
    consulta = ContratoCooperativa.objects.get(pk=pk)
    if request.POST:
        form = ContratoCooperativaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('/listadocontratocooperativa')
        else:
            return render(
                request,
                'contratoscooperativas/editar_contratocooperativa.html',
                {"form": form}
            )
    else:
        form = ContratoCooperativaForm(instance=consulta)
        return render(request,
            'contratoscooperativas/editar_contratocooperativa.html',
            {"form": form}
        )


# Create your views here.

