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
from login.views import FormularioLogin
from registros.views.Pagos.views import ListaPagos, FormularioPago
from registros.views.acudientes.views import ListaAcudientes
from registros.views.docentes.views import ListaDocentes
from registros.views.docentes.views import FormularioDocente
from registros.views.grados.views import ListaGrados, VistaFormularioGrado
from registros.views.jornada.views import ListaJornadas, VistaFormularioJornada
from registros.views.materias.views import ListaMaterias, FormularioMaterias
from registros.views.personas.views import ListaPersona, FormularioPersona
from registros.views.estudiante.views import ListaEstudiantes, FormularioEstudiante
from registros.views.domicilio.views import ListaDomicilios, FormularioDomicilio
from registros.views.matriculas.views import ListaMatriculas




urlpatterns = [
    path('admin/', admin.site.urls),
    path('personas/', ListaPersona.as_view(), name='listapersonas'),
    path('materias/', ListaMaterias.as_view(), name='listamaterias'),
    path('docentes/', ListaDocentes.as_view(), name='listadocentes'),
    path('pagos/', ListaPagos.as_view(), name='listapagos'),
    path('grados/', ListaGrados.as_view(), name='listagrado'),
    path('estudiantes/', ListaEstudiantes.as_view(), name='listaestudiantes'),
    path('jornadas/', ListaJornadas.as_view(), name='listajornada'),
    path('acudientes/', ListaAcudientes.as_view()),
    path('domicilios/', ListaDomicilios.as_view(), name='listadomicilios'),
    path('matriculas/', ListaMatriculas.as_view()),
    path('crear_persona/', FormularioPersona.as_view(), name='formulariopersona'),
    path('crear_materia/', FormularioMaterias.as_view(), name='formulariomaterias'),
    path('crear_estudiante/', FormularioEstudiante.as_view(), name='formularioestudiante'),
    path('crear_docente/', FormularioDocente.as_view(), name='formulariodocente'),
    path('crear_domicilio/', FormularioDomicilio.as_view(), name='formulariodomicilio'),
    path('crear_pago/', FormularioPago.as_view(), name='formulariopago'),
    path('crear_jornada/', VistaFormularioJornada.as_view(), name='formulariojornada'),
    path('crear_grado/', VistaFormularioGrado.as_view(), name='formulariogrado'),
    path('login/', FormularioLogin.as_view()),

    
    



]
