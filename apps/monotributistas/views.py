from django.shortcuts import render, redirect

from .forms import MonotributistaForm
from .models import Monotributista


def listadomonotributista(request):
    if "txtbuscar" in request.GET:
        parametro = request.GET.get("txtbuscar")
        resultados = Monotributista.objects.filter(apellido__contains=parametro)
    else:
        resultados = Monotributista.objects.all().order_by("apellido")

    return render(
        request,
        "monotributistas/lista_monotributista.html",
        {
            "resultados": resultados
        })


def nuevomonotributista(request):
    if request.POST:
        form = MonotributistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listadomonotributista')
        else:
            return render(request, 'monotributistas/editar_monotributista.html', {"form": form})
    else:
        form = MonotributistaForm()
        return render(request, 'monotributistas/editar_monotributista.html', {"form": form})


def editarmonotributista(request, pk):
    consulta = Monotributista.objects.get(pk=pk)
    if request.POST:
        form = MonotributistaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('/listadomonotributista')
        else:
            return render(
                request,
                'monotributistas/editar_monotributista.html',
                {"form": form}
            )
    else:
        form = MonotributistaForm(instance=consulta)
        return render(request, 'monotributistas/editar_monotributista.html', {"form": form})


# Create your views here.
