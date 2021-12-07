from django import forms

from PuntoVentas.models import FlatFile


class FileForm(forms.ModelForm):
    class Meta:
        model = FlatFile
        fields = ['title', 'typeFile', 'description', 'file', ]
