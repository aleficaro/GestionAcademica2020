from django.db import models
from datetime import datetime


# Create your models here.
from django.forms import model_to_dict


class Persona(models.Model):
    dni = models.CharField(max_length=15, primary_key=True, verbose_name='DNI')
    nombres = models.CharField(max_length=50, verbose_name='Nombres')
    #s_nombre = models.CharField(max_length=50, verbose_name='Segundo nombre', null=True, blank=True)
    apellidos = models.CharField(max_length=50, verbose_name='Apellidos')
    #s_apellido = models.CharField(max_length=50, verbose_name='Segundo apellido', null=True, blank=True)
    genero = models.CharField(max_length=30, verbose_name='Genero', choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')])
    edad = models.SmallIntegerField(verbose_name='Edad')
    correo = models.EmailField(max_length=70, verbose_name='Correo')
    telefono = models.CharField(max_length=30, verbose_name='Telefono')
    #foto = models.ImageField('Foto', upload_to='imagenes', null=True, blank='')
    eps = models.CharField(max_length=100, null=True, blank=True, verbose_name='EPS')
    fe_registro = models.DateField(default=datetime.now, verbose_name='Fecha de registro')

    # se definio el metodo para mostrarel nombre completo de persona, este metodo se puede llamar desde otros metodos que esten relacionados
    def nombrecompleto(self):
        nc = '{} {}'.format(self.nombres, self.apellidos)
        return nc


    # Se crea el metodo toJSON para covertir el modelo a JSON
    def toJSON(self):
        jpersonas = model_to_dict(self)
        # se inidica el nombre del campo ['nombres'] utilizado en el ajax, donde se mostrara la informacion.
        jpersonas['nombres'] = '{}'.format(self.nombrecompleto())
        jpersonas['genero'] = self.get_genero_display()
        return jpersonas

    def __str__(self):
        txt = "{} {}"
        return txt.format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'Persona'
        ordering = ['nombres']


class Estudiante(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    id_estudiante = models.CharField(max_length=15, primary_key=True, verbose_name='id')
    t_sangre = models.CharField(max_length=20, choices=[('AP', 'A positivo'), ('AN', 'A negativo'), ('OP', 'O positivo'), ('ON', 'O negativo')])
    discapacidad = models.CharField(max_length=20, choices=[('Sordo', 'Sordo'), ('Mudo', 'Mudo'), ('Ciego', 'Ciego'), ('Timido', 'Timido'), ('Ninguno', 'Ninguno')])
    vigencia = models.BooleanField(default=True)

    def __str__(self):
        txt = '{}'.format(self.persona)
        return txt


    def toJSON(self):
        t_estudiantes = model_to_dict(self)
        t_estudiantes['persona'] = '{}'.format(self.persona.nombrecompleto())

        return t_estudiantes

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        db_table = 'estudiante'
        ordering = ['id_estudiante']


class Docente(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    id_docente = models.CharField(max_length=10, default=5000, primary_key=True, verbose_name='id')
    profesion = models.CharField(max_length=50, verbose_name='Profesión', null=True, blank=False)
    contrato = models.CharField(max_length=20, choices=[('IDF', 'Indefinido'), ('PS', 'Prestación de servicios'), ('An', 'Anual'), ('ETC', 'etc')])

    def __str__(self):
        txt = '{}'.format(self.persona)
        return txt

    def toJSON(self):
        jdocente = model_to_dict(self)
        jdocente['persona'] = '{}'.format(self.persona.nombrecompleto())
        return jdocente

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        db_table = 'docente'
        ordering = ['id_docente']


class Pago(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    id_pago = models.CharField(max_length=10, primary_key=True, verbose_name='id pago')
    v_pago = models.IntegerField(verbose_name='Valor de pago', default=0)
    fe_pago = models.DateField(default=datetime.now, editable=False, verbose_name='Fecha de pago')
    tipo_pago = models.CharField(max_length=20, null=True, choices=[('Efectivo', 'Efectivo'), ('Banco', 'Banco'), ('Transferencia','Tranferencia')])

    def __str__(self):
        txt = '{} '.format(self.estudiante.persona.nombrecompleto()) # nombre de quien realizo pago en la vista admin
        return txt

    def toJSON(self):
        tpagos = model_to_dict(self)
        tpagos['fe_pago'] = self.fe_pago.strftime('%d-%m-%y') # convertir fecha a str
        tpagos['estudiante'] = self.estudiante.persona.nombrecompleto() # se envia el nombre de quien pago a la lista
        return tpagos

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        db_table = 'pago'
        ordering = ['id_pago']


class Jornada(models.Model):
    id_jornada = models.CharField(verbose_name='Id jornada', primary_key=True, default='', max_length=20)
    jornada = models.CharField('Jornada', max_length=50, choices=[('Mañana', 'Mañana'), ('Tarde', 'Tarde'), ('Noche', 'Noche')])

    def __str__(self):
        txt = '{}'.format(self.jornada)
        return txt

    def toJSON(self):
        jjornada = model_to_dict(self)
        return jjornada

    class Meta:
        verbose_name = 'Jornada'
        verbose_name_plural = 'Jornadas'
        db_table = 'jornada'
        ordering = ['jornada']


class Grado(models.Model):
    jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE)
    id_grado = models.CharField(verbose_name='Id grado', max_length=10, unique=True, primary_key=True)
    n_grado = models.CharField('Grado', max_length=30)
    capacidad = models.IntegerField('Capacidad', default=30)

    def __str__(self):
        txt = '{}'.format(self.n_grado)
        return txt

    def toJSON(self):
        jgrados = model_to_dict(self)
        jgrados['jornada']= '{}'.format(self.jornada)
        return jgrados

    class Meta:
        verbose_name = 'Grados'
        verbose_name_plural = 'Grados'
        db_table = 'grado'
        ordering = ['id_grado']


class Acudiente(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    id_acudiente = models.CharField('Id Acudiente', primary_key=True, max_length=20)
    parentesco = models.CharField('Parentesco', default='', max_length=30, choices=[('Padre', 'Padre'), ('Madre', 'Madre'), ('Hermano', 'Hermano'), ('Tio', 'Tio')])
    ocupacion = models.CharField('Ocupación', default='', max_length=50, choices=[('Ingeniero', 'Ingeniero'), ('Abogado', 'Abogado'), ('Independiente', 'independiente')])

    def __str__(self):
        txt = 'cedula {}: {} es el {} de {}'.format(self.persona.dni, self.persona, self.parentesco, self.estudiante)

        return txt



    def toJSON(self):
        jacudiente = model_to_dict(self)
        jacudiente['persona'] = '{}'.format(self.persona)
        jacudiente['estudiante'] = '{}'.format(self.estudiante)
        jacudiente['id_acudiente'] = '{}'.format(self.persona.dni)
        return jacudiente

    class Meta:
        verbose_name = 'Acudiente'
        verbose_name_plural = 'Acudientes'
        db_table = 'acudiente'
        ordering = ['id_acudiente']


class Domicilio(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    id_domicilio = models.CharField('Id domicilio', max_length=15, primary_key=True, unique=True)
    pais = models.CharField('Pais', max_length=50, null=True, default='Colombia')
    departamento = models.CharField('Departamento', max_length=50, null=True, default='Cauca')
    ciudad = models.CharField('Ciudad', max_length=50, null=True, default='Popayan')
    barrio = models.CharField('Barrio', max_length=50, null=True, default='')
    direccion = models.CharField('Dirección', max_length=50, null=True, default='')

    def __str__(self):
        txt = '{} {} {} '.format(self.ciudad, self.barrio, self.direccion)
        return txt

    def toJSON(self):
        jdomicilio = model_to_dict(self)
        jdomicilio['persona'] = '{}'.format(self.persona.nombrecompleto()) # se modifica el valor que va en la columna de la lista
        return jdomicilio

    class Meta:
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domicilios'
        db_table = 'domicilio'
        ordering = ['id_domicilio']


class Materia(models.Model):
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE, default='')
    id_materia = models.CharField('Id materia', primary_key=True, default='', max_length=30)
    nmateria = models.CharField('Materia', max_length=50, null=True, default='')
    intensidad = models.IntegerField('Intensidad', null=True, default=4)

    def __str__(self):
        txt = '{}'.format(self.nmateria)
        return txt

    def toJSON(self):
        jmateria = model_to_dict(self)
        jmateria['nmateria'] = '{}'.format(self.nmateria) # se modifica el valor que va en la columna de la lista
        jmateria['intensidad'] = '{} horas'.format(self.intensidad) # se modifica el valor que va en la columna de la lista
        jmateria['grado'] = '{}'.format(self.grado) # se modifica el valor que va en la columna de la lista
        return jmateria

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
        db_table = 'materia'
        ordering = ['id_materia']


class Matricula(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    grado = models.ForeignKey(Grado, null=False, blank=False, on_delete=models.CASCADE)
    fecha_matricula = models.DateField(default=datetime.now, editable=False, verbose_name='Fecha de matricula')


    def __str__(self):
        txt = '{} {} {} {}'.format(self.id_matricula, self.estudiante, self.grado, self.fecha_matricula)
        return txt

    def toJSON(self):
        jmatricula = model_to_dict(self)
        jmatricula['fecha_matricula'] = self.fecha_matricula.strftime('%d-%m-%y')
        jmatricula['grado'] = '{}'.format(self.grado.n_grado)
        jmatricula['estudiante'] = '{}'.format(self.estudiante)
        jmatricula['id_matricula'] = '{}'.format(self.estudiante.persona.dni)
        return jmatricula

    class Meta:
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'
        db_table = 'matricula'
        ordering = ['id_matricula']
