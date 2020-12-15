from django.forms import ModelForm

from registros.models import Grado


class FormularioGrado(ModelForm):
    def __init__(self, *args, **kwargs):  # se sobreescribe la clase ModelForm del metodo __init__
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():  # Se crea un bucle para mostrar todos los campos(fiels)
            form.field.widget.attrs['class'] = 'form-control'  # A todos los campos se les asigna la clase form-control
            form.field.widget.attrs['autocomplete'] = 'off'  # Se desactiva la ayuda de autocompletado de los campos
        self.fields['id_grado'].widget.attrs['autofocus'] = True  # se hace el llamado a todos los componenetes con self y se le indica el campo donde debe estar el cursor

    class Meta:
        model = Grado
        fields = '__all__'  # Se cargan todos los campos del modelo en el formulario
        # Se utiliza esta propiedad de los formularios en django para personalizar los campos

