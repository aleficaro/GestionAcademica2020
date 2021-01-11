from django.contrib import admin

# Register your models here.
from app.core.registros.models import *

admin.site.register(Persona)
admin.site.register(Docente)
admin.site.register(Pago)
admin.site.register(Estudiante)
admin.site.register(Jornada)
admin.site.register(Grado)
admin.site.register(Acudiente)
admin.site.register(Domicilio)
admin.site.register(Materia)
admin.site.register(Matricula)
