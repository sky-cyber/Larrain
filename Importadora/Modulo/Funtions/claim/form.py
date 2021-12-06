from django.forms import *
from PuntoVentas.models import Contact


class ClaimForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Contact
        fields = '__all__'

    def clean(self):
        cleaned = super(ClaimForm, self).clean()
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        claim = self.cleaned_data.get('claim')

        if len(name) <= 2:
            raise forms.ValidationError('El Nombre debe tener minimo 2 caracteres')
        if not phone.isdigit():
            raise forms.ValidationError('No aceptamos caracteres, Simbolos Especiales ni Números Negativos en el Campo Teléfono')
        if len(phone) < 9:
            raise forms.ValidationError('Teléfono Invalido, Solo aceptamos 9 digitos')
        if len(claim) < 30:
            raise forms.ValidationError('Por favor se necesita mas información En el Campo Comentario para el envío de su solicitud')
        if len(claim) > 300:
            raise forms.ValidationError('Ha superdado el límite, no aceptamos más de 300 caracteres para su solicitud')
        return cleaned