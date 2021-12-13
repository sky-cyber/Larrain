from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Modulo.Funtions.category.form import CategoryForm
from django.contrib import messages

from PuntoVentas.mixins import ValidatorPermissionRequiredMixins
from PuntoVentas.models import *


def category_list(request):
    data = {
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)


class CategoryListView(LoginRequiredMixin, ValidatorPermissionRequiredMixins, ListView):
    model = Category
    template_name = "category/list.html"
    permission_required = 'view_category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado De Categorías"
        context['title2'] = "Categorías Registradas"
        context['object_list'] = Category.objects.all()
        context['url_create'] = reverse_lazy('category_create')
        context['button'] = "Nuevo Registro"
        context['button2'] = "Generar PDF"
        return context


class CategoryCreateView(LoginRequiredMixin, ValidatorPermissionRequiredMixins, CreateView):
    model = Category
    template_name = "category/create.html"
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')
    permission_required = 'add_category'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                # form = CategoryForm(request.POST)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = "No ha ingresado ninguna opción"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Crear Categoría"
        context['title2'] = "Agregue Su Categoría"
        context['button'] = "Guardar Registro"
        context['list'] = reverse_lazy('category_list')
        context['button2'] = "Volver al Listado"
        context['action'] = 'add'
        return context


class CategoryUpdateView(LoginRequiredMixin, ValidatorPermissionRequiredMixins, UpdateView):
    model = Category
    template_name = "category/create.html"
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')
    permission_required = 'change_category'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CategoryUpdateView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = "No Ha Selecionado Ninguna Opción"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edición de la Categoría"
        context['title2'] = "Edite Su Categoría"
        context['button'] = "Actualizar Categoría"
        context['list'] = reverse_lazy('category_list')
        context['button2'] = "Volver al Listado"
        context['action'] = 'edit'
        return context


class CategoryDeleteView(LoginRequiredMixin, ValidatorPermissionRequiredMixins, DeleteView):
    model = Category
    template_name = "category/delete.html"
    success_url = reverse_lazy('category_list')
    permission_required = 'delete_category'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CategoryDeleteView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminación de una Categoría"
        context['title2'] = "¿Quiere eliminar la categoría "
        context['url_list'] = reverse_lazy('category_list')
        return context
