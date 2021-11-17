from django.shortcuts import render

# Create your function here.
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.core.paginator import Paginator

from PuntoVentas.models import *


def home(request):
    category = Category.objects.all()
    if request.user.is_authenticated:
        user = request.user
        order, created = Orders.objects.get_or_create(user=user, isPaid=False, isDelivered=False)
        items = order.oderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    context = {'items': items, 'order': order, 'category': category}
    return render(request, 'Web/home.html', context)


class DashboardView(TemplateView):
    template_name = 'Adm/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Total de Registros'
        context['totalProduct'] = Product.objects.count()
        context['totalUsers'] = User.objects.count()
        context['totalSupplier'] = Supplier.objects.count()
        context['totalOrder'] = Orders.objects.count()
        return context


class PerfilView(TemplateView):
    template_name = 'Adm/perfil.html'


def Catalogue(request):
    button = 'Agregar al Carrito'
    button1 = 'Ver Producto'
    object_list = Product.objects.all().order_by("-id")
    category = Category.objects.all()
    if request.user.is_authenticated:
        user = request.user
        order, created = Orders.objects.get_or_create(user=user, isPaid=False, isDelivered=False)
        items = order.oderitem_set.all()
        paginator = Paginator(object_list, 8)
        page = request.GET.get('page') or 1
        object_list = paginator.get_page(page)
        current_page = int(page)
        pages = range(1, object_list.paginator.num_pages + 1)
    else:
        order = []
        items = []
        paginator = Paginator(object_list, 8)
        page = request.GET.get('page') or 1
        object_list = paginator.get_page(page)
        current_page = int(page)
        pages = range(1, object_list.paginator.num_pages + 1)
    context = {'object_list': object_list, 'button': button,
               'button1': button1, 'order': order, 'items': items,
               'current_page': current_page, 'pages': pages, 'category': category}
    return render(request, 'Web/catalogue.html', context)


def ProductOffer(request):
    button = 'Agregar al Carrito'
    button1 = 'Ver Producto'
    productOffer = Product.objects.filter(offer=True).order_by("-id")
    category = Category.objects.all()
    if request.user.is_authenticated:
        user = request.user
        order, created = Orders.objects.get_or_create(user=user, isPaid=False, isDelivered=False)
        items = order.oderitem_set.all()
        paginator = Paginator(productOffer, 8)
        page = request.GET.get('page') or 1
        productOffer = paginator.get_page(page)
        current_page = int(page)
        pages = range(1, productOffer.paginator.num_pages + 1)
    else:
        order = []
        items = []
        paginator = Paginator(productOffer, 8)
        page = request.GET.get('page') or 1
        productOffer = paginator.get_page(page)
        current_page = int(page)
        pages = range(1, productOffer.paginator.num_pages + 1)
    context = {'productOffer': productOffer, 'button': button, 'button1': button1, 'category': category,
               'items': items, 'current_page': current_page, 'pages': pages, 'order': order}
    return render(request, 'Web/productOffer.html', context)


class AllCategoriesView(TemplateView):
    model = Category
    template_name = 'category/allcategories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        context['allcategories'] = Category.objects.all()
        context['category'] = category
        context['button'] = 'Agregar al Carrito'
        context['button1'] = 'Ver Producto'
        return context


class TypeCategory(TemplateView):
    model = Category
    template_name = 'category/typeCategory.html'

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            user = self.request.user
            order, created = Orders.objects.get_or_create(user=user, isPaid=False, isDelivered=False)
            items = order.oderitem_set.all()
        else:
            order = []
            items = []
        context = super(TypeCategory, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        categories = Category.objects.filter(slug=slug)
        category = Category.objects.all()
        context['categories'] = categories
        context['category'] = category
        context['order'] = order
        context['items'] = items
        context['button'] = 'Agregar al Carrito'
        context['button1'] = 'Ver Producto'
        return context


class ProductDetailView(TemplateView):
    model = Product
    template_name = 'Product/Detail_Product.html'

    def get_context_data(self, **kwargs, ):
        if self.request.user.is_authenticated:
            user = self.request.user
            order, created = Orders.objects.get_or_create(user=user, isPaid=False, isDelivered=False)
            items = order.oderitem_set.all()
        else:
            order = []
            items = []
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        product = Product.objects.get(slug=slug)
        category = Category.objects.all()
        product.numReviews += 1
        product.save()
        context['category'] = category
        context['product'] = product
        context['order'] = order
        context['items'] = items
        context['button'] = 'Agregar al Carrito'
        return context


def team(request):
    return render(request, 'web/team1.html')


def register(request):
    return render(request, 'web/contact.html')
