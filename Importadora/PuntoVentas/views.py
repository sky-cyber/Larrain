from django.shortcuts import render

# Create your function here.
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView

from PuntoVentas.models import Product, Category


def home(request):
    return render(request, 'Web/home.html')


def adm(request):
    return render(request, 'Adm/admin.html')


class CatalogueListView(ListView):
    model = Product
    template_name = 'Web/catalogue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Product.objects.all().order_by("-id")
        context['button'] = 'Agregar al Carrito'
        context['button1'] = 'Ver Producto'
        return context


class AllCategoriesView(TemplateView):
    model = Category
    template_name = 'category/allcategories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allcategories'] = Category.objects.all()
        context['button'] = 'Agregar al Carrito'
        context['button1'] = 'Ver Producto'
        return context


class ProductDetailView(TemplateView):
    model = Product
    template_name = 'Product/Detail_Product.html'

    def get_context_data(self, **kwargs, ):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        product = Product.objects.get(slug=slug)
        product.view_count += 1
        product.save()
        context['product'] = product
        return context


def team(request):
    return render(request, 'web/team.html')


def register(request):
    return render(request, 'web/register.html')
