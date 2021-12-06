from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from PuntoVentas.models import *
from PuntoVentas.mixins import ValidatorPermissionRequiredMixins


class OrderClientDetail(LoginRequiredMixin, ValidatorPermissionRequiredMixins, TemplateView):
    model = Orders
    template_name = 'Order/orderClientDetail.html'
    permission_required = 'view_orders'

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


class ChangeOrderView(ValidatorPermissionRequiredMixins, TemplateView):
    permission_required = 'change_orders'

    def post(self, request, *args, **kwargs):
        order_id = self.kwargs['pk']
        order = Orders.objects.get(id=order_id)
        new_status = request.POST.get("status")
        order.status = new_status
        order.save()
        return redirect(reverse_lazy('order_list'), kwargs={"pk": order_id})


class OrderListView(LoginRequiredMixin, ValidatorPermissionRequiredMixins, ListView):
    model = Orders
    template_name = 'Order/list.html'
    permission_required = 'view_orders'

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        allorder = Orders.objects.all().order_by("-id")
        context['allorder'] = allorder
        context['title'] = 'Listado de Todas Las Ordenes Emitidas'
        context['title2'] = 'Filtrado de Ordenes Registradas:'
        return context


class OrderComplete(LoginRequiredMixin, ValidatorPermissionRequiredMixins, TemplateView):
    model = Orders
    template_name = 'Order/orderComplete.html'
    permission_required = 'view_orders'

    def get_context_data(self, **kwargs):
        context = super(OrderComplete, self).get_context_data(**kwargs)
        context['object_list'] = Orders.objects.filter(status="Orden Completada").order_by("-id")
        context['title'] = 'Listado de Ordenes Completadas'
        context['title2'] = 'Filtrado de Ordenes Registradas:'
        return context


class OrderInProcess(LoginRequiredMixin, ValidatorPermissionRequiredMixins, TemplateView):
    model = Orders
    template_name = 'Order/orderInProcess.html'
    permission_required = 'view_orders'

    def get_context_data(self, **kwargs):
        context = super(OrderInProcess, self).get_context_data(**kwargs)
        context['object_list'] = Orders.objects.filter(status="Orden En Proceso").order_by("-id")
        context['title'] = 'Listado de Ordenes En Proceso'
        context['title2'] = 'Filtrado de Ordenes Registradas:'
        return context


class OrderToDispatch(LoginRequiredMixin, ValidatorPermissionRequiredMixins, TemplateView):
    model = Orders
    template_name = 'Order/orderToDispatch.html'
    permission_required = 'view_orders'

    def get_context_data(self, **kwargs):
        context = super(OrderToDispatch, self).get_context_data(**kwargs)
        context['object_list'] = Orders.objects.filter(status="Orden A Despacho")
        context['title'] = 'Listado de Ordenes A Despacho'
        context['title2'] = 'Filtrado de Ordenes Registradas:'
        return context


class OrderCanceled(LoginRequiredMixin, ValidatorPermissionRequiredMixins, TemplateView):
    model = Orders
    template_name = 'Order/orderCanceled.html'
    permission_required = 'view_orders'

    def get_context_data(self, **kwargs):
        context = super(OrderCanceled, self).get_context_data(**kwargs)
        context['object_list'] = Orders.objects.filter(status="Orden Cancelada")
        context['title'] = 'Listado de Ordenes Canceladas'
        context['title2'] = 'Filtrado de Ordenes Registradas:'
        return context


class OrderOnTheWay(LoginRequiredMixin, ValidatorPermissionRequiredMixins, TemplateView):
    model = Orders
    template_name = 'Order/orderOnTheWay.html'
    permission_required = 'view_orders'

    def get_context_data(self, **kwargs):
        context = super(OrderOnTheWay, self).get_context_data(**kwargs)
        context['object_list'] = Orders.objects.filter(status="Orden En Camino")
        context['title'] = 'Listado de Ordenes En Camino'
        context['title2'] = 'Filtrado de Ordenes Registradas:'
        return context
