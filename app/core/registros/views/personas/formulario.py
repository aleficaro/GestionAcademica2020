from django.forms import *

from app.core.registros.models import Persona


class Formulariopersona(ModelForm):

    def __init__(self, *args, **kwargs):  # se sobreescribe la clase ModelForm del metodo __init__
        super().__init__(*args, **kwargs)
        for form in self.visible_fields(): # Se crea un bucle para mostrar todos los campos(fields)
            form.field.widget.attrs['class'] = 'form-control' # A todos los campos se les asigna la clase form-control
            form.field.widget.attrs['autocomplete'] = 'off' # Se desactiva la ayuda de autocompletado de los campos
        self.fields['dni'].widget.attrs['autofocus'] = True # se hace el llamdo a todos los componenetes con self y se le indica el campo donde debe estar el cursor

    class Meta:
        model = Persona
        fields = '__all__' # Se cargan todos los campos del modelo en el formulario
        # Se utiliza esta propiedad de los formularios en django para personalizar los campos
        widgets = {
            'dni': TextInput(
                attrs = {
                    'placeholder' : 'Número de identificación' # Se le asigna una descripcioon dentro del campo
                }
            ),
            'nombres': TextInput(
                attrs={
                    'placeholder': 'Escribe tus nombres'
                }
            ),
            'apellidos': TextInput(
                attrs={
                    'placeholder': 'Escribe tus apellidos'
                }
            ),
            'edad': TextInput(
                attrs={
                    'placeholder': 'Ingresa tu edad'
                }
            ),
            'correo': TextInput(
                attrs={
                    'placeholder': 'Escribe tú correo'
                }
            ),
            'telefono': TextInput(
                attrs={
                    'placeholder': 'Escribe tu teléfono'
                }
            ),
            'eps': TextInput(
                attrs={
                    'placeholder': 'Escribe tu EPS si tienes'
                }
            ),
        }

