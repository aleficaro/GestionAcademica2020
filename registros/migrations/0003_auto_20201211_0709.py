# Generated by Django 3.1.4 on 2020-12-11 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0002_auto_20201201_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='id_docente',
            field=models.AutoField(default=5000, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
