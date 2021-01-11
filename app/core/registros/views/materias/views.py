from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from app.core.registros.models import Materia
from django.views.generic import ListView, CreateView

from app.core.registros.views.materias.formulario import FormularioMateria


class ListaMaterias(ListView):
    model = Materia
    template_name = 'listas/listamaterias.html'
    success_url = reverse_lazy('formulariomaterias')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscarmateria':
                data = []
                for i in Materia.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Materias'
        context['url_nuevo_registro'] = success_url = reverse_lazy('formulariomaterias')
        return context


class FormularioMaterias(CreateView):
    model = Materia
    form_class = FormularioMateria
    template_name = 'formularios/formmateria.html'
    success_url = reverse_lazy('listamaterias')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Materia'
        context['url_nuevo_registro'] = success_url = reverse_lazy('formulariomaterias') # se crea url para utilizarla en el boton nuevo registro
        context['url_cancelar'] = success_url = reverse_lazy('listamaterias') # se crea url para utilizarla en el boton nuevo registro
        return context