from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from PuntoVentas.models import *


class OrderListView(ListView):
    model = Orders
    template_name = 'Order/list.html'

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        context['object_list'] = Orders.objects.all().order_by('-id')
        context['title'] = 'Listado de Ordenes Emitidas'
        context['title2'] = 'Ordenes Registradas'
        context['button2'] = 'Generar PDF'
        return context


class OrderClientDetail(TemplateView):
    model = Orders
    template_name = 'Order/orderClientDetail.html'

    def get_context_data(self, **kwargs):
        context = super(OrderClientDetail, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        order = Orders.objects.get(pk=pk)
        context['order'] = order
        context['items'] = order.oderitem_set.all()
        context['shipping'] = ShippingAddress.objects.get(order=order)
        context['allstatus'] = ORDER_STATUS
        context['button'] = "Volver al Listado de Ordenes"
        context['PDF'] = "Generar PDF"
        return context


class ChangeOrderView(TemplateView):
    def post(self, request, *args, **kwargs):
        order_id = self.kwargs['pk']
        order = Orders.objects.get(id=order_id)
        new_status = request.POST.get("status")
        order.status = new_status
        order.save()
        return redirect(reverse_lazy('order_list'), kwargs={"pk": order_id})

