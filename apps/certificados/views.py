
from django.shortcuts import render, redirect

from lib.numeroatexto import numtxt
from .forms import CertificadoForm
from .models import Certificado
from apps.contratosobras.models import ContratoObra


def listadocertificadoobra(request):
    if "txtbuscar" in request.GET:
        parametro = request.GET.get("txtbuscar")
        resultados = Certificado.objects.filter(contratista__descripcion__contains=parametro)
    else:
        resultados = Certificado.objects.all()
    return render(
        request,
        "certificados/lista_certificadoobra.html",
        {
            "resultados": resultados
        })


def nuevocertificadoobra(request):
    if request.POST:
        form = CertificadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listadocertificadoobra')
        else:
            return render(request, 'certificados/editar_certificadoobra.html', {"form": form})
    else:
        form = CertificadoForm()
        return render(request, 'certificados/editar_certificadoobra.html', {"form": form})


def editarcertificadoobra(request, pk):
    consulta = Certificado.objects.get(pk=pk)
    if request.POST:
        form = ContratoObraForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('/listadocontratoobra')
        else:
            return render(
                request,
                'contratosobras/editar_contratoobra.html',
                {"form": form}
            )
    else:
        form = ContratoObraForm(instance=consulta)
        return render(request,
            'contratosobras/editar_contratoobra.html',
            {"form": form}
        )


def detalleresolucionobra(request, pk):
    try:
        resultados = Certificado.objects.get(pk=pk)
        montocontrato = ContratoObra.objects.get(obra=resultados.obra.pk)
        letramonto = numtxt(resultados.monto)
        avance = float(resultados.monto) / float(montocontrato.monto)
        avance = round(float(avance * 100),2)
        
        return render(
            request,
            'certificados/resolucion.html',
            {
                "resultados": resultados,
                "letramonto": letramonto,
                "avance": avance
            }
        )
         
    except:
        return render(
            request,
            'certificados/404.html',
        )
        
    

    

# Create your views here.
