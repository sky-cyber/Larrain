# Generated by Django 3.2.7 on 2021-10-03 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PuntoVentas', '0005_auto_20211003_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='Password',
            field=models.CharField(default='', max_length=200, verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(max_length=200, verbose_name='Apellidos'),
        ),
    ]
