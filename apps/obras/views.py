
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from .forms import ObraForm
from .models import Obra


def listadoobra(request):
    if 'txtBuscar' in request.GET:
        parametro = request.GET.get('txtBuscar')
        consulta = Obra.objects.filter(
            descripcion__icontains=parametro
        ).order_by('descripcion')
    else:
        consulta = Obra.objects.all().order_by('descripcion')
    paginador = Paginator(consulta, 20)
    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1
    resultados = paginador.get_page(page)
    return render(request, 'obras/obra_list.html', {'resultados': resultados})
 

def nuevaobra(request):
    if request.POST:
        form = ObraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA GRABADO LA OBRA")
            return redirect('/obralistado')
        else:
            return render(request, 'obras/obra_edit.html', {"form": form})
    else:
        form = ObraForm()
        return render(request, 'obras/obra_edit.html', {"form": form})


def editarobra(request, pk):
    consulta = Obra.objects.get(pk=pk)
    if request.POST:
        form = ObraForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA ACTUALIZADO LA OBRA SOCIAL")
            return redirect('/obralistado')
        else:
            return render(request, 'obras/obra_edit.html', {"form": form})
    else:
        form = ObraForm(instance=consulta)
        return render(request, 'obras/obra_edit.html', {"form": form})

# Create your views here.
