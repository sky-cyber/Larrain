# Generated by Django 3.2.7 on 2021-12-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PuntoVentas', '0009_alter_supplier_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='dispatch',
            field=models.CharField(choices=[('Manuel Rodrigo Osandon Rubilar', 'Manuel Rodrigo Osandon Rubilar'), ('Jose Rolando Vergara Quinteros', 'Jose Rolando Vergara Quinteros'), ('Bernardo Ramon Valdivia Sepulveda', 'Bernardo Ramon Valdivia Sepulveda'), ('Joselin Paulina Muñoz Aranda', 'Joselin Paulina Muñoz Aranda'), ('Ester Romina Faundes Mendez', 'Ester Romina Faundes Mendez'), ('Luz Carmen Rivas Perez', 'Luz Carmen Rivas Perez'), ('Stephany Roxana Segovia Miranda', 'Stephany Roxana Segovia Miranda'), ('Carlos Fabian Rosales Marambio', 'Carlos Fabian Rosales Marambio'), ('Paula Andrea Belice Asturias', 'Paula Andrea Belice Asturias'), ('Rodrigo Bastian Romero Castillo', 'Rodrigo Bastian Romero Castillo')], default='', max_length=100),
        ),
    ]
