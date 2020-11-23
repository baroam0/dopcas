
from django.shortcuts import render, redirect


from .forms import ContratoObraForm
from .models import ContratoObra


def detallecontratoobra(request, pk):
    resultado = ContratoObra.objects.get(pk=pk)

    return render(request,
        'contratosobras/contrato_licitacion.html',
        {
            "resultado": resultado
        }
    )




def listadocontratoobra(request):
    if "txtbuscar" in request.GET:
        parametro = request.GET.get("txtbuscar")
        resultados = ContratoObra.objects.filter(obra__descripcion__contains=parametro)
    else:
        resultados = ContratoObra.objects.all()
    return render(
        request,
        "contratosobras/lista_contratoobra.html",
        {
            "resultados": resultados
        })


def nuevocontratoobra(request):
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


def editarcontratoobra(request, pk):
    consulta = ContratoObra.objects.get(pk=pk)
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
