
from django.shortcuts import render, redirect

from .forms import ContratoMonotributistaForm
from .models import ContratoMonotributista
from apps.complementos.models import Mes
from apps.tiposcontratos.models import TipoContrato
from lib.numeroatexto import numtxt, numerotxt
from lib.cuentames import totalmes


def detallecontrato(request, pk):
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

    
def listadocontratomonotributista(request):
    if "txtbuscar" in request.GET:
        parametro = request.GET.get("txtbuscar")
        resultados = ContratoMonotributista.objects.filter(monotributista__apellido__contains=parametro)
    else:
        #resultados = ContratoMonotributista.objects.all().order_by("fecha_inicio")
        resultados = ContratoMonotributista.objects.filter(cumplimentado=False)
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
        form = ContratoMonotributistaForm(instance=consulta)
        return render(request, 'contratomonotributistas/editar_contratomonotributista.html', {"form": form})


def generaf16b(request):
    meses = Mes.objects.all().order_by("pk")
    contratos = ContratoMonotributista.objects.all().order_by("monotributista")
    return render(
        request,
        'monotributistas/generaf16b.html',
        {
            "contratos": contratos,
            "meses": meses
        })


def f16b(request,cnt,mes):
    contrato = ContratoMonotributista.objects.get(pk=cnt)
    mes = Mes.objects.get(pk=mes)
    return render(
        request,
        'monotributistas/f16b.html',
        {
            "contrato": contrato,
            "mes": mes
        }
    )

# Create your views here.
