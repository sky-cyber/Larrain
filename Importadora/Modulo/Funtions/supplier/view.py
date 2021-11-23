from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from Modulo.Funtions.supplier.form import SupplierForm
from PuntoVentas.models import *
from PuntoVentas.mixins import ValidatorPermissionRequiredMixins


class SupplierListView(LoginRequiredMixin, ValidatorPermissionRequiredMixins, ListView):
    model = Supplier
    template_name = "Supplier/list.html"
    permission_required = 'view_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado De los Contratos"
        context['title2'] = "Proveedores Registrados"
        context['object_list'] = Supplier.objects.all()
        context['url_create_supplier'] = reverse_lazy('supplier_create')
        context['button'] = "Nuevo Registro"
        context['button2'] = "Generar PDF"
        return context


class SupplierCreateView(LoginRequiredMixin, ValidatorPermissionRequiredMixins, CreateView):
    model = Supplier
    template_name = "Supplier/create.html"
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_list')
    permission_required = 'add_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Registrar un Proveedor"
        context['title2'] = "Agregue un Proveedor"
        context['button'] = "Guardar Registro"
        return context


class SupplierUpdateView(LoginRequiredMixin, ValidatorPermissionRequiredMixins, UpdateView):
    model = Supplier
    template_name = "Supplier/create.html"
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_list')
    permission_required = 'change_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modificar Proveedor"
        context['title2'] = "Edite Su Proveedor"
        context['button'] = "Actualizar Datos"
        return context


class SupplierDeleteView(LoginRequiredMixin, ValidatorPermissionRequiredMixins, DeleteView):
    model = Supplier
    template_name = "Supplier/delete.html"
    success_url = reverse_lazy('supplier_list')
    permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminación de un Proveedor"
        context['title2'] = "¿Quiere eliminar al Proveedor "
        context['url_list_supplier'] = reverse_lazy('supplier_list')
        return context


class ContractSupplier(LoginRequiredMixin, ValidatorPermissionRequiredMixins, TemplateView):
    model = Supplier
    template_name = "Supplier/contract.html"
    permission_required = 'view_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['contract'] = Supplier.objects.get(pk=pk)
        context['button'] = "Volver a la lista de Provedores"
        context['PDF'] = "Generar PDF"
        return context





