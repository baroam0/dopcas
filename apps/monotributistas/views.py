from django.shortcuts import render

from .models import Monotributista

def listadomonotributista(request):
    resultado = Monotributista.objects.all()
    print(resultado)
    return render(
        request,
        "monotributistas/lista_monotributista.html",
        {
            "resultado": resultado
        })
    


# Create your views here.
