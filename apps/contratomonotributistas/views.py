
from django.shortcuts import render, redirect

from .forms import ContratoMonotributistaForm
from .models import ContratoMonotributista
from apps.tiposcontratos.models import TipoContrato
from lib.numeroatexto import numtxt
from lib.cuentames import totalmes


def detallecontrato(request, pk):
    resultado = ContratoMonotributista.objects.get(pk=pk)
    tipocontrato = TipoContrato.objects.get(pk=int(resultado.tipocontrato.pk))
    plazo = totalmes(resultado.fecha_inicio, resultado.fecha_fin)
    montocontrato = plazo * resultado.monto_mensual
    letramontocontrato = numtxt(montocontrato)
    
    if tipocontrato.descripcion == "Contrato Administrativo":
        return render(
            request,
            "tiposcontratos/contrato_administrativo.html",
            {
                "resultado": resultado,
                "plazo": plazo,
                "montocontrato": montocontrato,
                "letramontocontrato": letramontocontrato
            }
        )


def listadocontratomonotributista(request):
    if "txtbuscar" in request.GET:
        parametro = request.GET.get("txtbuscar")
        resultados = ContratoMonotributista.objects.filter(monotributista__apellido__contains=parametro)
    else:
        resultados = ContratoMonotributista.objects.all().order_by("fecha_inicio")
    return render(
        request,
        "contratomonotributistas/lista_contratomonotributista.html",
        {
            "resultados": resultados
        })


def nuevocontratomonotributista(request):
    if request.POST:
        form = ContratoMonotributistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listadocontratomonotributista')
        else:
            return render(request, 'contratomonotributistas/editar_contratomonotributista.html', {"form": form})
    else:
        form = ContratoMonotributistaForm()
        return render(request, 'contratomonotributistas/editar_contratomonotributista.html', {"form": form})


def editarcontratomonotributista(request, pk):
    consulta = ContratoMonotributista.objects.get(pk=pk)
    if request.POST:
        form = ContratoMonotributistaForm(request.POST, instance=consulta)
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
        form = MonotributistaForm(instance=consulta)
        return render(request, 'contratomonotributistas/editar_contratomonotributista.html', {"form": form})


# Create your views here.
