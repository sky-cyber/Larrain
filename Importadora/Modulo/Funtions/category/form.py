from django.forms import *
from PuntoVentas.models import Category


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': 'Nombre de la categoria',
            'slug': 'Etiqueta'
        }
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese Caterogria'
                }
            ),
            'slug': TextInput(
                attrs={
                    'placeholder': 'Ingrese Etiqueta'
                }
            )
        }


