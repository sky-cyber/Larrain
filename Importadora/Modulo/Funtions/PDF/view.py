from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import View
from weasyprint import HTML, CSS
import os
from PuntoVentas.models import *

from Importadora import settings


class ProductPdfView(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template("PDF/productPDF.html")
            context = {"product": Product.objects.all(),
                       "name": "Wykep",
                       "rut": "17.984.014-6",
                       "Company": "Importadora Larrain",
                       "address": "Avenida porvenir #679",
                       "title": "Listado de productos",
                       'icon': '{}{}'.format(settings.MEDIA_URL, 'logo_wykep_ori.png')}
            html_template = template.render(context)
            css_url = os.path.join(settings.BASE_DIR, 'static/admin/css/bootstrap.min.css')
            pdf = HTML(string=html_template, base_url=request.build_absolute_uri()).write_pdf(
                stylesheets=[CSS(css_url)])
            return HttpResponse(pdf, content_type='application/pdf')
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('home'))


class SupplierPdfView(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template("PDF/supplierPDF.html")
            context = {"supplier": Supplier.objects.all(),
                       "name": "Wykep",
                       "rut": "17.984.014-6",
                       "Company": "Importadora Larrain",
                       "address": "Avenida porvenir #679",
                       "title": "Listado de Proveedores",
                       'icon': '{}{}'.format(settings.MEDIA_URL, 'logo_wykep_ori.png')}
            html_template = template.render(context)
            css_url = os.path.join(settings.BASE_DIR, 'static/admin/css/bootstrap.min.css')
            pdf = HTML(string=html_template, base_url=request.build_absolute_uri()).write_pdf(
                stylesheets=[CSS(css_url)])
            return HttpResponse(pdf, content_type='application/pdf')
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('home'))


class OrderPdfView(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template("PDF/orderPDF.html")
            pk = self.kwargs['pk']
            order = Orders.objects.get(pk=pk)
            context = {"order": order,
                       "items": order.oderitem_set.all(),
                       "shipping": ShippingAddress.objects.get(order=order),
                       "name": "Wykep",
                       "rut": "17.984.014-6",
                       "Telefóno": "+56 9 99632564",
                       "Web": "www.wykep.com",
                       "Company": "Importadora Larrain",
                       "address": "Avenida porvenir #679",
                       "title": "Listado de Proveedores",
                       'icon': '{}{}'.format(settings.MEDIA_URL, 'logo_wykep_ori.png')}
            html_template = template.render(context)
            css_url = os.path.join(settings.BASE_DIR, 'static/admin/css/bootstrap.min.css')
            pdf = HTML(string=html_template, base_url = request.build_absolute_uri()).write_pdf(stylesheets=[CSS(css_url)])
            return HttpResponse(pdf, content_type='application/pdf')
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('home'))


class ContractpdfView(View):
    def get(self, request, *args, **kwargs):
        try:
            templates = get_template("PDF/contractPDF.html")
            context = {"contract": Supplier.objects.get(pk=self.kwargs['pk']),
                       "Company": "Importadora Larrain",
                       "rut": "17.984.014-6",
                       "Telefóno": "+56 9 99632564",
                       "Web": "www.wykep.com",
                       "title": "CONTRATO COMERCIAL PROVEEDORES DE BIENES O PRODUCTOS",
                       "address": "Avenida porvenir #679",
                       'icon': '{}{}'.format(settings.MEDIA_URL, 'logo_wykep_ori.png')}
            html_template = templates.render(context)
            css_url = os.path.join(settings.BASE_DIR, 'static/admin/css/bootstrap.min.css')
            pdf = HTML(string=html_template, base_url=request.build_absolute_uri()).write_pdf(
                stylesheets=[CSS(css_url)])
            return HttpResponse(pdf, content_type='application/pdf')
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('home'))


class DispatchPdfView(View):
    def get(self, request, *args, **kwargs):
        # try:
            template = get_template("PDF/listDispatch.html")
            user = request.user
            order = Orders.objects.filter(status="Orden A Despacho")
            shipping = ShippingAddress.objects.all()
            context = {"order": order,
                       "user": user,
                       "shipping": shipping,
                       "name": "Wykep",
                       "rut": "17.984.014-6",
                       "Telefóno": "+56 9 99632564",
                       "Web": "www.wykep.com",
                       "Company": "Importadora Larrain",
                       "address": "Avenida porvenir #679",
                       "title": "Listado de Proveedores",
                       'icon': '{}{}'.format(settings.MEDIA_URL, 'logo_wykep_ori.png')}
            html_template = template.render(context)
            css_url = os.path.join(settings.BASE_DIR, 'static/admin/css/bootstrap.min.css')
            pdf = HTML(string=html_template, base_url = request.build_absolute_uri()).write_pdf(stylesheets=[CSS(css_url)])
            return HttpResponse(pdf, content_type='application/pdf')
        # except:
        #     pass
        # return HttpResponseRedirect(reverse_lazy('home'))