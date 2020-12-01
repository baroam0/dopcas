
from django.shortcuts import render

from .models import Certificado


def listadocertificadoobra(request):
    if "txtbuscar" in request.GET:
        parametro = request.GET.get("txtbuscar")
        resultados = Certificado.objects.filter(contratista__descripcion__contains=parametro)
    else:
        resultados = Certificado.objects.all()
    return render(
        request,
        "certificados/lista_contratoobra.html",
        {
            "resultados": resultados
        })


def nuevocertificadoobra(request):
    if request.POST:
        form = ContratoObraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listadocontratoobra')
        else:
            return render(request, 'contratosobras/editar_contratoobra.html', {"form": form})
    else:
        form = ContratoObraForm()
        return render(request, 'contratosobras/editar_contratoobra.html', {"form": form})


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






# Create your views here.
