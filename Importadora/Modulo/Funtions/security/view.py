from Importadora.wsgi import *
from django.contrib.auth.views import LoginView, FormView
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView

from Modulo.Funtions.security.form import CreateUserForm, ResetPasswordForm
from PuntoVentas.models import *

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.contrib.auth.models import User
from django.template.loader import render_to_string

from Importadora import settings


class LoginFormView(LoginView):
    template_name = 'Security/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super(LoginFormView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Acceso Al Sistema'
        return context


def RegisterUser(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'Security/register.html', context)


def RegisterUserAdmin(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                form.save()
                return redirect('adm')
    context = {'form': form}
    return render(request, 'Security/registerAdmin.html', context)


class ResetPasswordView(FormView):
    template_name = 'Security/resetPassword.html'
    form_class = ResetPasswordForm
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def dispatch(self, request, *args, **kwargs):
        return super(ResetPasswordView, self).dispatch(request, *args, **kwargs)

    def send_email_reset_Password(self, user):
        data = {}
        try:
            mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            mailServer.starttls()
            mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

            email_to = user.email

            # Construimos el mensaje simple
            mensaje = MIMEMultipart()
            mensaje['From'] = settings.EMAIL_HOST_USER
            mensaje['To'] = email_to
            mensaje['Subject'] = "Reseteo de contraseña"

            content = render_to_string('Email/sendResetPassword.html', {
                'user': user,
                'link_resetpwd': '',
                'link_home': ''
            })
            # Adjuntamos el texto
            mensaje.attach(MIMEText(content, 'html'))

            # Envio del mensaje
            mailServer.sendmail(settings.EMAIL_HOST_USER,
                                email_to,
                                mensaje.as_string())
        except Exception as e:
            data['error'] = str(e)
        return data

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = ResetPasswordForm(request.POST)
            if form.is_valid():
                user = form.get_user()
                data = self.send_email_reset_Password(user)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super(ResetPasswordView, self).get_context_data(**kwargs)
        context['title'] = 'Reseteo de Contraseña'
        context['title2'] = 'Ingrese Su Nombre de Usuario que utilizó ' \
                            'al crear su cuenta. Se enviará un correo electrónico ' \
                            'a ese usuario con más instrucciones sobre cómo ' \
                            'restablecer su contraseña.'
        return context


class UserListView(ListView):
    model = User
    template_name = "Security/list.html"

    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado De Categorias"
        context['title2'] = "Categorias Registradas"
        context['object_list'] = User.objects.all()
        context['url_create'] = reverse_lazy('category_create')
        context['button'] = "Nuevo Registro"
        return context
