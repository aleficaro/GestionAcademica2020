# Generated by Django 3.1.4 on 2020-12-12 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0009_auto_20201211_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='id_pago',
            field=models.AutoField(default='1000', primary_key=True, serialize=False, verbose_name='id pago'),
        ),
    ]
