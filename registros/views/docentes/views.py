from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from registros.models import Docente
from django.forms import model_to_dict

from registros.views.docentes.formulario import FormularioDocente


class ListaDocentes(ListView):
    model = Docente
    template_name = 'listas/listadocentes.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def toJSON(self):
        jdocentes = model_to_dict(self)
        return jdocentes

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscardato':
                data = []
                for i in Docente.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Docentes'
        context['url_nuevo_registro'] = success_url = reverse_lazy('formulariodocente') # se direciona al formulario de docente
        return context

class FormularioDocente(CreateView):
    model = Docente
    form_class = FormularioDocente
    template_name = 'formularios/formdocente.html'
    success_url = reverse_lazy('listadocentes')

    @method_decorator(login_required)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear docente'
        context['url_nuevo_registro'] = success_url = reverse_lazy('formulariodocente') # se crea url para utilizarla en el boton nuevo registro
        return context