# Generated by Django 3.2.7 on 2021-10-30 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PuntoVentas', '0007_auto_20211029_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='deliveredAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='paidAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
