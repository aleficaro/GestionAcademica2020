# Generated by Django 3.1.4 on 2020-12-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0003_auto_20201211_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acudiente',
            name='id_acudiente',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id Acudiente'),
        ),
        migrations.AlterField(
            model_name='domicilio',
            name='id_domicilio',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id domicilio'),
        ),
        migrations.AlterField(
            model_name='grado',
            name='id_grado',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id grado'),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='id_jornada',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id jornada'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='id_pago',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id pago'),
        ),
    ]
