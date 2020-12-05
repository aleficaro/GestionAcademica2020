from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from registros.models import Estudiante
from registros.views.estudiante.formulario import FormularioEstudiante


class ListaEstudiantes(ListView):
    model = Estudiante
    template_name = 'listas/listaestudiantes.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscardato':
                data = []
                for i in Estudiante.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Estudiantes'
        return context

class FormularioEstudiante(CreateView):
    model = Estudiante
    template_name = 'formularios/formestudiante.html'
    form_class = FormularioEstudiante
    success_url = reverse_lazy('listaestudiantes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear estudiante'
        context['url_nuevo_registro'] = success_url = reverse_lazy('formularioestudiante') # se crea url para utilizarla en el boton nuevo registro
        return context