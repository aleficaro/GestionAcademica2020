from select import select

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


from registros.models import Persona
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from registros.views.personas.formulario import Formulariopersona


class ListaPersona(ListView):
    model = Persona
    template_name = 'listas/listapersonas.html'
    success_url = reverse_lazy('formulario')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscarpersona':
                data = []
                for i in Persona.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Personas'
        context['url_nuevo_registro'] = success_url = reverse_lazy('formulariopersona') # se crea url para utilizarla en el boton nuevo registro
        return context


class FormularioPersona(CreateView):
    model = Persona
    form_class = Formulariopersona
    template_name = 'formularios/formpersona.html' #Fomulario que se utlizara para la creacion
    success_url = reverse_lazy('listapersonas') # Muestra la pagina de listado al seleccionar guardar. En la url se le debe poner el name paras ser llamad desde aqui.



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear persona' #titulo de la pestaña y del card
        context['url_nuevo_registro'] = success_url = reverse_lazy('formulariopersona') # se crea url para utilizarla en el boton nuevo registro
        context['url_cancelar'] = success_url = reverse_lazy('listapersonas') # se crea url para utilizarla en el boton nuevo registro
        return context


class EditarPersona(UpdateView):
    model = Persona
    form_class = Persona
    template_name = 'formularios/formpersona.html'  # Fomulario que se utlizara para la creacion
    success_url = reverse_lazy('listapersonas')  # Muestra la pagina de listado al seleccionar guardar. En la url se le debe poner el name paras ser llamad desde aqui.

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'editar':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar persona'  # titulo de la pestaña y del card
        context['action'] = 'editar'
        context['url_editar_registro'] = success_url = reverse_lazy('formulariopersona') # se crea url para utilizarla en el boton nuevo registro

        return context
