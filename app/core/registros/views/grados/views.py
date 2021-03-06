from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView
from app.core.registros.models import Grado
from app.core.registros.views.grados.formulario import FormularioGrado


class ListaGrados(ListView):
    model = Grado
    template_name = 'listas/listagrados.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscardato':
                data = []
                for i in Grado.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Grados'
        context['url_nuevo_registro'] = success_url = reverse_lazy('formulariogrado')
        return context

class VistaFormularioGrado(CreateView):
    model = Grado
    template_name = 'formularios/formgrados.html'
    form_class = FormularioGrado
    success_url = reverse_lazy('listagrado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Grado'
        context['url_cancelar'] = success_url = reverse_lazy('listagrado')
        return context