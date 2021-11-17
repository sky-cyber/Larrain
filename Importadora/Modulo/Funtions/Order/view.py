from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from PuntoVentas.models import *


class OrderClientDetail(TemplateView):
    model = Orders
    template_name = 'Order/orderClientDetail.html'

    def get_context_data(self, **kwargs):
        context = super(OrderClientDetail, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        order = Orders.objects.get(pk=pk)
        context['order'] = order
        context['items'] = order.oderitem_set.all()
        if ShippingAddress.objects.filter(order=order).exists():
            context['shipping'] = ShippingAddress.objects.get(order=order)
        else:
            context['shipping'] = []
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


class OrderListView(ListView):
    model = Orders
    template_name = 'Order/list.html'

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        context['object_list'] = Orders.objects.all().order_by("-id")
        context['title'] = 'Listado de Todas Las Ordenes Emitidas'
        context['title2'] = 'Filtrado de Ordenes Registradas:'
        return context


class OrderComplete(TemplateView):
    model = Orders
    template_name = 'Order/orderComplete.html'

    def get_context_data(self, **kwargs):
        context = super(OrderComplete, self).get_context_data(**kwargs)
        context['object_list'] = Orders.objects.filter(status="Orden Completada").order_by("-id")
        context['title'] = 'Listado de Ordenes Completadas'
        context['title2'] = 'Filtrado de Ordenes Registradas:'
        return context


class OrderInProcess(TemplateView):
    model = Orders
    template_name = 'Order/orderInProcess.html'

    def get_context_data(self, **kwargs):
        context = super(OrderInProcess, self).get_context_data(**kwargs)
        context['object_list'] = Orders.objects.filter(status="Orden En Proceso").order_by("-id")
        context['title'] = 'Listado de Ordenes En Proceso'
        context['title2'] = 'Filtrado de Ordenes Registradas:'
        return context


class OrderToDispatch(TemplateView):
    model = Orders
    template_name = 'Order/orderToDispatch.html'

    def get_context_data(self, **kwargs):
        context = super(OrderToDispatch, self).get_context_data(**kwargs)
        context['object_list'] = Orders.objects.filter(status="Orden A Despacho")
        context['title'] = 'Listado de Ordenes A Despacho'
        context['title2'] = 'Filtrado de Ordenes Registradas:'
        return context


class OrderCanceled(TemplateView):
    model = Orders
    template_name = 'Order/orderCanceled.html'

    def get_context_data(self, **kwargs):
        context = super(OrderCanceled, self).get_context_data(**kwargs)
        context['object_list'] = Orders.objects.filter(status="Orden Cancelada")
        context['title'] = 'Listado de Ordenes Canceladas'
        context['title2'] = 'Filtrado de Ordenes Registradas:'
        return context


class OrderOnTheWay(TemplateView):
    model = Orders
    template_name = 'Order/orderOnTheWay.html'

    def get_context_data(self, **kwargs):
        context = super(OrderOnTheWay, self).get_context_data(**kwargs)
        context['object_list'] = Orders.objects.filter(status="Orden En Camino")
        context['title'] = 'Listado de Ordenes En Camino'
        context['title2'] = 'Filtrado de Ordenes Registradas:'
        return context
