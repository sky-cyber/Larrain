from django import forms

from django.contrib.auth.forms import UserCreationForm
from PuntoVentas.models import User
from django.forms import model_to_dict


class CreateUserForm(UserCreationForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for form in self.visible_fields():
    #         form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'image', 'is_superuser', 'is_staff']
        exclude = ['last_login', 'date_joined', 'user_permissions']

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'groups', 'user_permissions'])
        item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.last_login.strftime('%Y-%m-%d')
        return item


class ResetPasswordForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese su Nombre de Usuario',
        'class': 'form-control'
    }))

    def clean(self):
        cleaned = super().clean()
        if not User.objects.filter(username=cleaned['username']).exists():
            self._errors['error'] = self._errors.get('error', self.error_class())
            self._errors['error'].append('El Nombre de Usuario no esta registrado')
            #raise forms.ValidationError('El email no existe')
        return cleaned

    def get_user(self):
        username = self.cleaned_data.get('username')
        return User.objects.get(username=username)


class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese una Contraseña',
        'class': 'form-control'
    }))
    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repita la contraseña',
        'class': 'form-control'
    }))

    def clean(self):
        cleaned = super().clean()
        password = cleaned['password']
        confirmPassword = cleaned['confirmPassword']
        if password != confirmPassword:
            self._errors['error'] = self._errors.get('error', self.error_class())
            self._errors['error'].append('Las credenciales no coinciden')
        return cleaned





