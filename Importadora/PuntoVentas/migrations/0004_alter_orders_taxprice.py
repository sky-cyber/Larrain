# Generated by Django 3.2.7 on 2021-11-08 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PuntoVentas', '0003_auto_20211108_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='taxPrice',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]