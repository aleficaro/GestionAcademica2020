from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from registros.models import Materia
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from registros.views.materias.formulario import FormularioMateria


class ListaMaterias(ListView):
    model = Materia
    template_name = 'listas/listamaterias.html'

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
        return context