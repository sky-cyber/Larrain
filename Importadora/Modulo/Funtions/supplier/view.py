from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Modulo.Funtions.supplier.form import SupplierForm
from PuntoVentas.models import *


# def category_list(request):
#     data = {
#         'categories': Category.objects.all()
#     }
#     return render(request, 'category/list.html', data)


class SupplierListView(ListView):
    model = Supplier
    template_name = "Supplier/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado De Proveedores"
        context['title2'] = "Proveedores Registrados"
        context['object_list'] = Supplier.objects.all()
        context['url_create_supplier'] = reverse_lazy('supplier_create')
        context['button'] = "Nuevo Registro"
        context['button2'] = "Generar PDF"
        return context


class SupplierCreateView(CreateView):
    model = Supplier
    template_name = "Supplier/create.html"
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Registrar un Proveedor"
        context['title2'] = "Agregue un Proveedor"
        context['button'] = "Guardar Registro"
        return context


class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = "Supplier/create.html"
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modificar Proveedor"
        context['title2'] = "Edite Su Proveedor"
        context['button'] = "Actualizar Datos"
        return context


class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = "Supplier/delete.html"
    success_url = reverse_lazy('supplier_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminación de un Proveedor"
        context['title2'] = "¿Quiere eliminar la Compañia "
        context['url_list_supplier'] = reverse_lazy('supplier_list')
        return context