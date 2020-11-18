
from django.shortcuts import render

from .forms import ContratistaForm
from .models import Contratista


def listadocontratista(request):
    if "txtbuscar" in request.GET:
        parametro = request.GET.get("txtbuscar")
        resultados = Contratista.objects.filter(descripcion__contains=parametro)
    else:
        resultados = Contratista.objects.all().order_by("descripcion")
    return render(
        request,
        "cooperativas/lista_cooperativa.html",
        {
            "resultados": resultados
        })


def nuevocontratista(request):
    if request.POST:
        form = ContratistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listadocontratista')
        else:
            return render(request, 'cooperativas/editar_cooperativa.html', {"form": form})
    else:
        form = ContratistaForm()
        return render(request, 'cooperativas/editar_cooperativa.html', {"form": form})


def editarcontratista(request, pk):
    consulta = Contratista.objects.get(pk=pk)
    if request.POST:
        form = ContratistaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('/listadocontratomonotributista')
        else:
            return render(
                request,
                'cooperativas/editar_cooperativa.html',
                {"form": form}
            )
    else:
        form = ContratistaForm(instance=consulta)
        return render(request, 'cooperativas/editar_cooperativa.html', {"form": form})





# Create your views here.
