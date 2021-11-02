from django.urls import reverse_lazy

from Modulo.Funtions.product.form import ProductForm
from PuntoVentas.models import Product

from django.views.generic import CreateView, ListView, UpdateView, DeleteView


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'Product/create.html'
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Product.objects.all()
        context['title'] = 'Agregar Nuevo Producto'
        context['title2'] = 'Registro'
        context['button'] = 'Guardar Registro'
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'Product/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Product.objects.all()
        context['title'] = 'Listado de Productos Registrados'
        context['title2'] = 'Productos Almacenados en Bodega'
        context['button'] = 'Agregar Producto'
        context['button2'] = 'Generar PDF'
        return context


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'Product/create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Producto'
        context['title2'] = 'Editar'
        context['button'] = 'Guardar Nuevo Registro'
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "Product/delete.html"
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminación de un producto"
        context['title2'] = "¿Quiere eliminar El Producto "
        context['product_url'] = reverse_lazy('product_list')
        return context








