from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Modulo.Funtions.category.form import CategoryForm
from PuntoVentas.models import *


def category_list(request):
    data = {
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)


class CategoryListView(ListView):
    model = Category
    template_name = "category/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado De Categorias"
        context['title2'] = "Categorias Registradas"
        context['object_list'] = Category.objects.all()
        context['url_create'] = reverse_lazy('category_create')
        context['button'] = "Nuevo Registro"
        context['button2'] = "Generar PDF"
        return context


class CategoryCreateView(CreateView):
    model = Category
    template_name = "category/create.html"
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Crear Categoria"
        context['title2'] = "Agregue Su Categoria"
        context['button'] = "Guardar Registro"
        return context


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = "category/create.html"
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edición de la Categoria"
        context['title2'] = "Edite Su Categoria"
        context['button'] = "Actualizar Categoria"
        return context


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "category/delete.html"
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminación de una Categoria"
        context['title2'] = "¿Quiere eliminar la categoria "
        context['url_list'] = reverse_lazy('category_list')
        return context