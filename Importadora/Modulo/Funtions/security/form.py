from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, PasswordInput, ModelForm

from PuntoVentas.models import User


class CreateUserForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for form in self.visible_fields():
    #         form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'image', 'is_superuser', 'is_staff']
        exclude = ['last_login', 'date_joined', 'user_permissions']

        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'password': 'Contraseña',
        }
        widgets = {
            'username': TextInput(
                attrs={
                    'placeholder': 'Ingrese su Nombre de Usuario',
                    'class': 'form-control'
                }
            ),
            'first_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus Nombres',
                    'class': 'form-control'
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus Apellidos',
                    'class': 'form-control'
                }
            ),
            'email': TextInput(
                attrs={
                    'placeholder': 'Ingrese Su correo Electronico',
                    'class': 'form-control'
                }
            ),
            'password': PasswordInput(render_value=True,
                attrs={
                    'placeholder': 'Ingrese una contraseña',
                    'class': 'form-control'
                }
            )
        }

    def clean(self):
        cleaned = super(CreateUserForm, self).clean()
        password = self.cleaned_data.get('password')
        username = self.cleaned_data.get('username')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if len(password) < 8:
            raise forms.ValidationError('La contraseña debe tener 8 caracteres')
        if len(username) < 3:
            raise forms.ValidationError('Nombre de usuario debe tener minimo 3 caracteres')
        if len(first_name) < 2:
            raise forms.ValidationError('Los nombres deben tener minimo 2 caracteres')
        if len(last_name) < 3:
            raise forms.ValidationError('Los apellidos deben tener minimo 3 caracteres')
        return cleaned

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


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
        if len(password) < 8:
            raise forms.ValidationError('Las claves debe tener un minimo de 8 caracteres')
        return cleaned
