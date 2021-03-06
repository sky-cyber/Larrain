from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from Modulo.Funtions.product.form import ProductForm
from PuntoVentas.models import Product

from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from PuntoVentas.mixins import ValidatorPermissionRequiredMixins


class ProductCreateView(LoginRequiredMixin, ValidatorPermissionRequiredMixins, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'Product/create.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'add_product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Product.objects.all()
        context['title'] = 'Agregar Nuevo Producto'
        context['title2'] = 'Registro'
        context['button'] = 'Guardar Registro'

        return context


class ProductListOfferView(LoginRequiredMixin, ValidatorPermissionRequiredMixins, ListView):
    model = Product
    template_name = 'Product/listOfferProduct.html'
    permission_required = 'view_product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Product.objects.filter(offer=True)
        context['title'] = 'Listado de Productos en Oferta'
        context['title2'] = 'Productos Almacenados en Bodega'
        context['button'] = 'Agregar Producto'
        context['button2'] = 'Generar PDF'
        return context


class ProductListView(LoginRequiredMixin, ValidatorPermissionRequiredMixins, ListView):
    model = Product
    template_name = 'Product/list.html'
    permission_required = 'view_product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Product.objects.all()
        context['title'] = 'Listado de Productos Registrados'
        context['title2'] = 'Productos Almacenados en Bodega'
        context['button'] = 'Agregar Producto'
        context['button2'] = 'Generar PDF'
        return context


class ProductUpdateView(LoginRequiredMixin, ValidatorPermissionRequiredMixins, UpdateView):
    model = Product
    template_name = 'Product/create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'change_product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edici??n de Producto'
        context['title2'] = 'Ha solicitado editar este producto'
        context['button'] = 'Guardar Nuevo Registro'
        return context


class ProductDeleteView(LoginRequiredMixin, ValidatorPermissionRequiredMixins, DeleteView):
    model = Product
    template_name = "Product/delete.html"
    success_url = reverse_lazy('product_list')
    permission_required = 'delete_product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminaci??n de un producto"
        context['title2'] = "??Quiere eliminar el producto "
        context['product_url'] = reverse_lazy('product_list')
        return context


class DetailProduct(TemplateView):
    model = Product
    template_name = 'Product/admin_detail_product.html'

    def get_context_data(self, **kwargs):
        context = super(DetailProduct, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        product = Product.objects.get(pk=pk)
        context['product'] = product
        return context







