from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from PuntoVentas.models import *


class DispatchList(TemplateView):
    model = Orders
    template_name = 'Dispatch/transferList.html'

    def get_context_data(self, **kwargs):
        context = super(DispatchList, self).get_context_data(**kwargs)
        dispatch = Orders.objects.filter(status="Orden A Despacho")
        context['dispatch'] = dispatch
        context['title'] = "Lista de Traslado"
        context['title2'] = "Ordenes listas Para Su Despacho"
        context['button'] = "Generar Lista"
        return context


class DispatchListComplete(TemplateView):
    model = Orders
    template_name = 'Dispatch/dispatchComplete.html'

    def get_context_data(self, **kwargs):
        context = super(DispatchListComplete, self).get_context_data(**kwargs)
        dispatch = Orders.objects.filter(status="Orden Completada")
        context['dispatch'] = dispatch
        context['title'] = "Lista de Ordenes Completadas"
        context['title2'] = "Pedidos Terminados"
        return context


class DispatchListInTheWay(TemplateView):
    model = Orders
    template_name = 'Dispatch/dispatchInTheWay.html'

    def get_context_data(self, **kwargs):
        context = super(DispatchListInTheWay, self).get_context_data(**kwargs)
        dispatch = Orders.objects.filter(status="Orden En Camino")
        context['dispatch'] = dispatch
        context['title'] = "Lista de Ordenes En Camino A Su Destino"
        context['title2'] = "Pedidos En Camino"
        return context


class DetailClient(TemplateView):
    model = Orders
    template_name = 'Dispatch/detailClient.html'

    def get_context_data(self, **kwargs):
        context = super(DetailClient, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        order = Orders.objects.get(pk=pk)
        items = order.oderitem_set.all()
        shipping = ShippingAddress.objects.get(order=order)
        context['order'] = order
        context['items'] = items
        context['shipping'] = shipping
        context['allstatus'] = ORDER_STATUS
        context['update_date'] = order.arrivalDate
        context['button'] = "Volver a la lista"
        return context


class ChangedispatchView(TemplateView):
    def post(self, request, *args, **kwargs):
        id_dispatch = self.kwargs['pk']
        order = Orders.objects.get(id=id_dispatch)
        new_status = request.POST.get("status")
        update_date = request.POST.get("arrivalDate")
        print(update_date)
        print(new_status)
        order.arrivalDate = update_date
        order.status = new_status
        order.save()
        return redirect(reverse_lazy('dispatch_list'), kwargs={"pk": id_dispatch})

