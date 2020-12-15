from django.contrib.auth.views import LoginView
from django.shortcuts import render


# Create your views here.
class FormularioLogin(LoginView):

    template_name = 'login.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # se obtienetodo lo que tiene el contex data
        context['title'] = 'Iniciar sesión'
        return context
