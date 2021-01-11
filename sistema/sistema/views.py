from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, FormView, TemplateView


class VistaSistema(TemplateView):
    template_name = 'templateBase2/listadocentes.html'
