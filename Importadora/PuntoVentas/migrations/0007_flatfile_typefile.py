# Generated by Django 3.2.7 on 2021-12-07 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PuntoVentas', '0006_auto_20211206_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatfile',
            name='typeFile',
            field=models.CharField(choices=[('Word', 'Word'), ('Excel', 'Excel'), ('PDF', 'PDF'), ('PNG', 'PNG'), ('Power Point', 'Power Point'), ('TXT', 'TXT')], default='', max_length=50, verbose_name='Tipo de Archivo'),
        ),
    ]
