from django.views.generic import ListView
from PuntoVentas.models import *


class OrderListView(ListView):
    model = Orders
    template_name = 'Order/list.html'

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        context['object_list'] = Orders.objects.all()
        context['title'] = 'Listado de Ordenes Emitidas'
        context['title2'] = 'Ordenes Registradas'
        context['button2'] = 'Generar PDF'
        return context
