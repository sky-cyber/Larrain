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
                       "name": "Brian Nuñez",
                       "rut": "17.984.014-6",
                       "Company": "Importadora Larrain",
                       "address": "Avenida porvenir #679",
                       "title": "Listado de productos",
                       'icon': '{}{}'.format(settings.MEDIA_URL, 'logo_wykep_ori.png')}
            html_template = template.render(context)
            css_url = os.path.join(settings.BASE_DIR, 'static/admin/css/bootstrap.min.css')
            pdf = HTML(string=html_template, base_url=request.build_absolute_uri()).write_pdf(stylesheets=[CSS(css_url)])
            return HttpResponse(pdf, content_type='application/pdf')
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('home'))


class SupplierPdfView(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template("PDF/supplierPDF.html")
            context = {"supplier": Supplier.objects.all(),
                       "name": "Brian Nuñez",
                       "rut": "17.984.014-6",
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
