from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect


# Create your views here.
class FormularioLogin(LoginView):
    template_name = 'login.html'


    # Funcion para validar que el usuario ya esta logueado
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated: #si el usuario esta autenticado entonces
            return redirect('/admin') # retorne al template admin (puede ser cualquier plantilla)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # se obtienetodo lo que tiene el contex data
        context['title'] = 'Iniciar sesión'
        return context
