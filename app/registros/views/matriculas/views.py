from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from registros.models import Matricula


class ListaMatriculas(ListView): # Se utiliza la clase ListView para  crear una lista generica  del modelo en su template
    model = Matricula
    template_name = 'listas/listamatriculas.html' # Ubicacion de la plantilla donde se van a mostrar los datos

    @method_decorator(csrf_exempt)  #Decorador de la clase
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {} # Se crea variable que obtendra el objeto Json del modelo
        try:
            action = request.POST['action']
            if action == 'buscardato':
                data = []
                for i in Matricula.objects.all(): # i hace el recorrido por el objeto Joranada creado por listView
                    data.append(i.toJSON()) # al diccionario data se le agregan los valores a traves del metodo en el modelo toJSON
            else:
                data['error'] = 'Ha ocurrido un error' # Mensaje de error si no se cargar los valores
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False) # Ek metodo post retorna el JsonResponse a traves de la variable data.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Matriculas' # Se envia el titulo a traves del diccionario
        return context