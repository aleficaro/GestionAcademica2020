"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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


# Se registran las url para poder ser renderizadas
from registros.views.Pagos.views import ListaPagos
from registros.views.acudientes.views import ListaAcudientes
from registros.views.docentes.views import ListaDocentes

from registros.views.grados.views import ListaGrados
from registros.views.jornada.views import ListaJornadas
from registros.views.materias.views import ListaMaterias
from registros.views.personas.views import ListaPersona, FormularioPersona
from registros.views.estudiante.views import ListaEstudiantes, FormularioEstudiante
from registros.views.domicilio.views import ListaDomicilios
from registros.views.matriculas.views import ListaMatriculas



urlpatterns = [
    path('admin/', admin.site.urls),
    path('personas/', ListaPersona.as_view(), name='listapersonas'),
    path('materias/', ListaMaterias.as_view()),
    path('docentes/', ListaDocentes.as_view()),
    path('pagos/', ListaPagos.as_view()),
    path('grados/', ListaGrados.as_view()),
    path('estudiantes/', ListaEstudiantes.as_view(), name='listaestudiantes'),
    path('jornadas/', ListaJornadas.as_view()),
    path('acudientes/', ListaAcudientes.as_view()),
    path('domicilios/', ListaDomicilios.as_view()),
    path('matriculas/', ListaMatriculas.as_view()),
    path('crear_persona/', FormularioPersona.as_view(), name='formulariopersona'),
    path('crear_estudiante/', FormularioEstudiante.as_view(), name='formularioestudiante'),



]
