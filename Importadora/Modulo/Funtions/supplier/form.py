from django.forms import *

from PuntoVentas.models import Supplier


class SupplierForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for p in self.visible_fields():
    #         p.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Supplier
        fields = '__all__'

