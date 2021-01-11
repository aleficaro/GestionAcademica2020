from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView

from app.core.registros.models import Pago
from app.core.registros.views.Pagos.formulario import FormularioPago


class ListaPagos(ListView):
    model = Pago
    template_name = 'listas/listapagos.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscardato':
                data = []
                for i in Pago.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Pagos'
        context['url_nuevo_registro'] = success_url = reverse_lazy('formulariopago') # se crea url para utilizarla en el boton nuevo registro
        return context


class FormularioPago(CreateView):
    model = Pago
    form_class = FormularioPago
    template_name = 'formularios/formpago.html'
    success_url = reverse_lazy('listapagos')  # Url que dirige a la lista cuando se guarda

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Asignar Pago'
        #context['url_nuevo_registro'] = success_url = reverse_lazy('formulariopago')  # se crea url para utilizarla en el boton nuevo registro
        context['url_cancelar'] = success_url = reverse_lazy('listapagos')
        return context
