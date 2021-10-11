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