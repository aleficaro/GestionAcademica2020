# Generated by Django 3.1.4 on 2020-12-31 19:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id_estudiante', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='id')),
                ('t_sangre', models.CharField(choices=[('AP', 'A positivo'), ('AN', 'A negativo'), ('OP', 'O positivo'), ('ON', 'O negativo')], max_length=20)),
                ('discapacidad', models.CharField(choices=[('Sordo', 'Sordo'), ('Mudo', 'Mudo'), ('Ciego', 'Ciego'), ('Timido', 'Timido'), ('Ninguno', 'Ninguno')], max_length=20)),
                ('vigencia', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
                'db_table': 'estudiante',
                'ordering': ['id_estudiante'],
            },
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id_grado', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Id grado')),
                ('n_grado', models.CharField(max_length=30, verbose_name='Grado')),
                ('capacidad', models.IntegerField(default=30, verbose_name='Capacidad')),
            ],
            options={
                'verbose_name': 'Grados',
                'verbose_name_plural': 'Grados',
                'db_table': 'grado',
                'ordering': ['id_grado'],
            },
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id_jornada', models.CharField(default='', max_length=20, primary_key=True, serialize=False, verbose_name='Id jornada')),
                ('jornada', models.CharField(choices=[('Mañana', 'Mañana'), ('Tarde', 'Tarde'), ('Noche', 'Noche')], max_length=50, verbose_name='Jornada')),
            ],
            options={
                'verbose_name': 'Jornada',
                'verbose_name_plural': 'Jornadas',
                'db_table': 'jornada',
                'ordering': ['jornada'],
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('dni', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='DNI')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=30, verbose_name='Genero')),
                ('edad', models.SmallIntegerField(verbose_name='Edad')),
                ('correo', models.EmailField(max_length=70, verbose_name='Correo')),
                ('telefono', models.CharField(max_length=30, verbose_name='Telefono')),
                ('eps', models.CharField(blank=True, max_length=100, null=True, verbose_name='EPS')),
                ('fe_registro', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'db_table': 'Persona',
                'ordering': ['nombres'],
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='id pago')),
                ('v_pago', models.IntegerField(default=0, verbose_name='Valor de pago')),
                ('fe_pago', models.DateField(default=datetime.datetime.now, editable=False, verbose_name='Fecha de pago')),
                ('tipo_pago', models.CharField(choices=[('Efectivo', 'Efectivo'), ('Banco', 'Banco'), ('Transferencia', 'Tranferencia')], max_length=20, null=True)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.estudiante')),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Pagos',
                'db_table': 'pago',
                'ordering': ['id_pago'],
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id_matricula', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_matricula', models.DateField(default=datetime.datetime.now, editable=False, verbose_name='Fecha de matricula')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.estudiante')),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.grado')),
            ],
            options={
                'verbose_name': 'Matricula',
                'verbose_name_plural': 'Matriculas',
                'db_table': 'matricula',
                'ordering': ['id_matricula'],
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id_materia', models.CharField(default='', max_length=30, primary_key=True, serialize=False, verbose_name='Id materia')),
                ('nmateria', models.CharField(default='', max_length=50, null=True, verbose_name='Materia')),
                ('intensidad', models.IntegerField(default=4, null=True, verbose_name='Intensidad')),
                ('grado', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='registros.grado')),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
                'db_table': 'materia',
                'ordering': ['id_materia'],
            },
        ),
        migrations.AddField(
            model_name='grado',
            name='jornada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.jornada'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.persona'),
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id_domicilio', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='Id domicilio')),
                ('pais', models.CharField(default='Colombia', max_length=50, null=True, verbose_name='Pais')),
                ('departamento', models.CharField(default='Cauca', max_length=50, null=True, verbose_name='Departamento')),
                ('ciudad', models.CharField(default='Popayan', max_length=50, null=True, verbose_name='Ciudad')),
                ('barrio', models.CharField(default='', max_length=50, null=True, verbose_name='Barrio')),
                ('direccion', models.CharField(default='', max_length=50, null=True, verbose_name='Dirección')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.persona')),
            ],
            options={
                'verbose_name': 'Domicilio',
                'verbose_name_plural': 'Domicilios',
                'db_table': 'domicilio',
                'ordering': ['id_domicilio'],
            },
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id_docente', models.CharField(default=5000, max_length=10, primary_key=True, serialize=False, verbose_name='id')),
                ('profesion', models.CharField(max_length=50, null=True, verbose_name='Profesión')),
                ('contrato', models.CharField(choices=[('IDF', 'Indefinido'), ('PS', 'Prestación de servicios'), ('An', 'Anual'), ('ETC', 'etc')], max_length=20)),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registros.persona')),
            ],
            options={
                'verbose_name': 'Docente',
                'verbose_name_plural': 'Docentes',
                'db_table': 'docente',
                'ordering': ['id_docente'],
            },
        ),
        migrations.CreateModel(
            name='Acudiente',
            fields=[
                ('id_acudiente', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Id Acudiente')),
                ('parentesco', models.CharField(choices=[('padre', 'Padre'), ('madre', 'Madre'), ('hermano', 'Hermano'), ('tio', 'Tio')], default='', max_length=30, verbose_name='Parentesco')),
                ('ocupacion', models.CharField(choices=[('ingeniero', 'Ingeniero'), ('abogado', 'Abogado'), ('independiente', 'Independiente')], default='', max_length=50, verbose_name='Ocupación')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.estudiante')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.persona')),
            ],
            options={
                'verbose_name': 'Acudiente',
                'verbose_name_plural': 'Acudientes',
                'db_table': 'acudiente',
                'ordering': ['id_acudiente'],
            },
        ),
    ]
