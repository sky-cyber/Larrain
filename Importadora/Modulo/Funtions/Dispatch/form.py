from django.forms import *

from PuntoVentas.models import Dispatcher


class DispatcherForm(ModelForm):
    class Meta:
        model = Dispatcher
        fields = '__all__'

    def clean(self):
        cleaned = super(DispatcherForm, self).clean()
        first_name = self.cleaned_data.get('first_name')
        second_name = self.cleaned_data.get('second_name')
        pather_last_name = self.cleaned_data.get('pather_last_name')
        mother_last_name = self.cleaned_data.get('mother_last_name')
        phone = self.cleaned_data.get('phone')

        if not first_name.isalpha():
            raise forms.ValidationError(
                'No Aceptamos Números Ni Caracteres Especiales En El Primer Nombre, (Solo se acepta un solo valor ej: Brian)')
        if not second_name.isalpha():
            raise forms.ValidationError(
                'No Aceptamos Números Ni Caracteres Especiales En El Segundo Nombre, (Solo se acepta un solo valor ej: Miguel)')
        if not pather_last_name.isalpha():
            raise forms.ValidationError(
                'No Aceptamos Números Ni Caracteres Especiales En El Apellido Paterno, (Solo se acepta un solo valor ej: Nuñez)')
        if not mother_last_name.isalpha():
            raise forms.ValidationError(
                'No Aceptamos Números Ni Caracteres Especiales En El Apellido Materno, (Solo se acepta un solo valor ej: Herrera)')
        if len(first_name) < 2:
            raise forms.ValidationError('Primer Nombre debe tener minimo 2 caracteres')
        if len(second_name) < 2:
            raise forms.ValidationError('Segundo Nombre debe tener minimo 2 caracteres')
        if len(pather_last_name) < 3:
            raise forms.ValidationError('Apellido Paterno debe tener minimo 2 caracteres')
        if len(mother_last_name) < 3:
            raise forms.ValidationError('Apellido Materno debe tener minimo 3 caracteres')
        if not phone.isdigit():
            raise forms.ValidationError(
                'No aceptamos caracteres, Simbolos Especiales ni Números Negativos en el Campo Teléfono')
        if len(phone) < 9 or len(phone) > 9:
            raise forms.ValidationError('Teléfono Invalido, Solo aceptamos 9 digitos')
        return cleaned

