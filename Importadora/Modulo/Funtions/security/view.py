from django.contrib.admin import action
from django.contrib.auth.decorators import permission_required

from Importadora.wsgi import *
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, FormView
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt

from Modulo.Funtions.security.form import CreateUserForm, ResetPasswordForm, ChangePasswordForm
from PuntoVentas.models import *

import smtplib
import uuid
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
    title = "Registro de Usuarios"
    title2 = "Crear un Usuario Administrador"
    button = "Registar Usuario"
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                form.save()
                return redirect('list_user')
    context = {'form': form, 'title': title, 'title2': title2, 'button': button}
    return render(request, 'Security/registerAdmin.html', context)

# class RegisterUserAdmin(CreateView):
#     model = User
#     form_class = CreateUserForm
#     template_name = 'Security/registerAdmin.html'
#     # permission_required = 'user.add_user'
#     success_url = reverse_lazy('list_user')
#
#     # def dispatch(self, request, *args, **kwargs):
#     #     return super().dispatch(request, *args, **kwargs)
#
#     # def post(self, request, *args, **kwargs):
#     #     data = {}
#     #     try:
#     #         action = request.POST['action']
#     #         if action == 'add':
#     #             form = self.get_form()
#     #             data = form.save()
#     #         else:
#     #             data['error'] = 'No ha ingresado ninguna opción'
#     #     except Exception as e:
#     #         data['error'] = str(e)
#     #     return JsonResponse(data)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Creacion de un Usuario'
#         context['title2'] = 'Crear Usuario Administrador'
#         return context


class UpdateUserAdmin(UpdateView):
    model = User
    form_class = CreateUserForm
    template_name = 'Security/registerAdmin.html'
    permission_required = 'user.add_user'
    success_url = reverse_lazy('list_user')

    # def dispatch(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     return super().dispatch(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'edit':
    #             form = self.get_form()
    #             data = form.save()
    #         else:
    #             data['error'] = 'No ha ingresado ninguna opción'
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar un Usuario'
        context['title2'] = 'Edicion Usuario Administrador'
        context['button'] = 'Editar Usuario'
        return context


class DeleteUserAdmin(DeleteView):
    model = User
    form_class = CreateUserForm
    template_name = 'Security/delete.html'
    permission_required = 'user.add_user'
    success_url = reverse_lazy('list_user')

    # def dispatch(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     return super().dispatch(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'edit':
    #             form = self.get_form()
    #             data = form.save()
    #         else:
    #             data['error'] = 'No ha ingresado ninguna opción'
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Elimar un Usuario'
        context['title2'] = "¿Quiere eliminar al Usuario "
        return context


class ResetPasswordView(FormView):
    template_name = 'Security/resetPassword.html'
    form_class = ResetPasswordForm
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def dispatch(self, request, *args, **kwargs):
        return super(ResetPasswordView, self).dispatch(request, *args, **kwargs)

    def send_email_reset_Password(self, user):
        data = {}
        try:

            URL = settings.DOMAIN if not settings.DEBUG else self.request.META['HTTP_HOST']

            user.token = uuid.uuid4()
            user.save()

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
                'link_resetpwd': 'http://{}/changePassword/{}/'.format(URL, str(user.token)),
                'link_home': 'http://{}'.format(URL)
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
                return redirect('home')
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


class ChangePasswordView(FormView):
    form_class = ChangePasswordForm
    template_name = 'Security/changePassword.html'
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        token = self.kwargs['token']
        if User.objects.filter(token=token).exists():
            return super().get(request, *args, **kwargs)
        return HttpResponseRedirect(self.success_url)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = ChangePasswordForm(request.POST)
            if form.is_valid():
                user = User.objects.get(token=self.kwargs['token'])
                user.set_password(request.POST['password'])
                user.token = uuid.uuid4()
                user.save()
                return redirect(settings.LOGIN_URL)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super(ChangePasswordView, self).get_context_data(**kwargs)
        context['title'] = 'Cambio de Contraseña'
        context['button'] = 'Resetear'
        return context


class UserListView(ListView):
    model = User
    template_name = "Security/list.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in User.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado De Usuarios"
        context['title2'] = 'Lista de registros de Administradores'
        context['button'] = "Nuevo Registro"
        context['butto'] = "Generar PDF"
        return context
