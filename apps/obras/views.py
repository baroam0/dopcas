
from django.shortcuts import render, redirect

from .forms import ObraForm, AdjudicacionForm
from .models import Obra, Adjudicacion


def listadoobra(request):
    if "txtbuscar" in request.GET:
        parametro = request.GET.get("txtbuscar")
        resultados = Obra.objects.filter(descripcion__contains=parametro)
    else:
        resultados = Obra.objects.all().order_by("descripcion")
    return render(
        request,
        "obras/lista_obra.html",
        {
            "resultados": resultados
        })


def nuevaobra(request):
    if request.POST:
        form = ObraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listadoobra')
        else:
            return render(request, 'obras/editar_obra.html', {"form": form})
    else:
        form = ObraForm()
        return render(request, 'obras/editar_obra.html', {"form": form})


def editarobra(request, pk):
    consulta = Obra.objects.get(pk=pk)
    if request.POST:
        form = ObraForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('/listadoobra')
        else:
            return render(
                request,
                'obras/editar_obra.html',
                {"form": form}
            )
    else:
        form = ObraForm(instance=consulta)
        return render(request, 'obras/editar_obra.html', {"form": form})


def listadoadjudicacion(request):
    if "txtbuscar" in request.GET:
        parametro = request.GET.get("txtbuscar")
        resultados = Adjudicacion.objects.filter(obra__descripcion__contains=parametro)
    else:
        resultados = Adjudicacion.objects.all()
    return render(
        request,
        "obras/lista_adjudicacion.html",
        {
            "resultados": resultados
        })


def nuevaadjudicacion(request):
    if request.POST:
        form = AdjudicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listadoobra')
        else:
            return render(request, 'obras/editar_adjudicacion.html', {"form": form})
    else:
        form = AdjudicacionForm()
        return render(request, 'obras/editar_adjudicacion.html', {"form": form})


def editaradjudicacion(request, pk):
    consulta = Adjudicacion.objects.get(pk=pk)
    if request.POST:
        form = AdjudicacionForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('/listadoobra')
        else:
            return render(
                request,
                'obras/editar_adjudicacion.html',
                {"form": form}
            )
    else:
        form = AdjudicacionForm(instance=consulta)
        return render(request, 'obras/editar_adjudicacion.html', {"form": form})

# Create your views here.
