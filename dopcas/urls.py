"""dopcas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from apps.certificados.views import (listadocertificadoobra,
    nuevocertificadoobra, detalleresolucionobra)

from apps.cooperativas.views import (listadocontratista,
    nuevocontratista, editarcontratista)

from apps.contratocooperativas.views import (listadocontratocooperativa,
    nuevocontratocooperativa, editarcontratocooperativa, detallecontratocooperativa)

from apps.contratosobras.views import (listadocontratoobra, nuevocontratoobra,
    editarcontratoobra, detallecontratoobra)

from apps.contratomonotributistas.views import (detallecontrato,
    listadocontratomonotributista, nuevocontratomonotributista,
    editarcontratomonotributista, f16b, generaf16b)

from apps.monotributistas.views import (listadomonotributista,
    editarmonotributista, nuevomonotributista)

from apps.obras.views import (listadoobra, nuevaobra, editarobra)

from dopcas.views import inicio


urlpatterns = [
    path('', inicio),
    path('admin/', admin.site.urls),
    path('listadocontratista/', listadocontratista),
    path('nuevocontratista/', nuevocontratista),
    path('editarcontratista/<int:pk>', editarcontratista),
    
    path('listadocontratocooperativa/', listadocontratocooperativa),
    path('nuevocontratocooperativa/', nuevocontratocooperativa),
    path('editarcontratocooperativa/<int:pk>', editarcontratocooperativa),
    path('detallecontratocooperativa/<int:pk>/', detallecontratocooperativa),

    path('listadocontratoobra/', listadocontratoobra),
    path('nuevocontratoobra/', nuevocontratoobra),
    path('editarcontratoobra/<int:pk>', editarcontratoobra),
    path('detallecontratoobra/<int:pk>/', detallecontratoobra),
    
    path('listadoobra/', listadoobra),
    path('nuevaobra/', nuevaobra),
    path('editarobra/<int:pk>', editarobra),
    
    path('detallecontrato/<int:pk>/', detallecontrato),
    path('listadocontratomonotributista/', listadocontratomonotributista),
    path('nuevocontratomonotributista/', nuevocontratomonotributista),
    path('editarcontratomonotributista/<int:pk>', editarcontratomonotributista),
    path('listadomonotributista/', listadomonotributista),
    path('nuevomonotributista/', nuevomonotributista),
    path('editarmonotributista/<int:pk>', editarmonotributista),
    path('generaf16b/', generaf16b),
    path('f16b/<int:cnt>/<int:mes>', f16b),
    
    path('listadocertificadoobra/', listadocertificadoobra),
    path('nuevocertificadoobra/', nuevocertificadoobra),
    path('detalleresolucionobra/<int:pk>', detalleresolucionobra),
]

