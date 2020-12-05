from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from registros.models import Materia


class ListaMaterias(ListView):
    model = Materia
    template_name = 'listas/listamaterias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Materias'
        return context