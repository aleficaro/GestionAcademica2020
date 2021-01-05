from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from registros.models import *
from registros.views.domicilio.formulario import FormularioDomicilio


class ListaDomicilios(ListView):
    model = Domicilio
    template_name = 'listas/listadomicilios.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def toJSON(self):
        jdomicilios = model_to_dict(self)
        return jdomicilios

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscardato':
                data = []
                for i in Domicilio.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Domicilios'
        context['url_nuevo_registro'] = success_url = reverse_lazy('formulariodomicilio')
        return context

class FormularioDomicilio(CreateView):
    model = Domicilio
    form_class = FormularioDomicilio
    template_name = 'formularios/formdomicilio.html'
    success_url = reverse_lazy('listadomicilios')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Domicilio'
        context['url_nuevo_registro'] = success_url = reverse_lazy('formulariodomicilio')  # se crea url para utilizarla en el boton nuevo registro
        context['url_cancelar'] = success_url = reverse_lazy('listadomicilios')
        return context
