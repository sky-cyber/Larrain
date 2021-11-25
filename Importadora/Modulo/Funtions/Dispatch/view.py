from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from PuntoVentas.models import *
from PuntoVentas.mixins import ValidatorPermissionRequiredMixins
from Modulo.Funtions.Dispatch.form import DispatcherForm


class DispatchList(ValidatorPermissionRequiredMixins, TemplateView):
    model = Orders
    template_name = 'Dispatch/transferList.html'
    permission_required = 'view_orders'

    def get_context_data(self, **kwargs):
        context = super(DispatchList, self).get_context_data(**kwargs)
        dispatch = Orders.objects.filter(status="Orden A Despacho")
        context['dispatch'] = dispatch
        context['title'] = "Lista de Traslado"
        context['title2'] = "Ordenes listas Para Su Despacho"
        context['button'] = "Generar Lista"
        return context


class DispatchListComplete(ValidatorPermissionRequiredMixins, TemplateView):
    model = Orders
    template_name = 'Dispatch/dispatchComplete.html'
    permission_required = 'view_orders'

    def get_context_data(self, **kwargs):
        context = super(DispatchListComplete, self).get_context_data(**kwargs)
        dispatch = Orders.objects.filter(status="Orden Completada")
        context['dispatch'] = dispatch
        context['title'] = "Lista de Ordenes Completadas"
        context['title2'] = "Pedidos Terminados"
        return context


class DispatchListInTheWay(ValidatorPermissionRequiredMixins, TemplateView):
    model = Orders
    template_name = 'Dispatch/dispatchInTheWay.html'
    permission_required = 'view_orders'

    def get_context_data(self, **kwargs):
        context = super(DispatchListInTheWay, self).get_context_data(**kwargs)
        dispatch = Orders.objects.filter(status="Orden En Camino")
        context['dispatch'] = dispatch
        context['title'] = "Lista de Ordenes En Camino A Su Destino"
        context['title2'] = "Pedidos En Camino"
        return context


class DetailClient(ValidatorPermissionRequiredMixins, TemplateView):
    model = Orders
    template_name = 'Dispatch/detailClient.html'
    permission_required = 'view_orders'

    def get_context_data(self, **kwargs):
        context = super(DetailClient, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        order = Orders.objects.get(pk=pk)
        items = order.oderitem_set.all()
        shipping = ShippingAddress.objects.get(order=order)
        date = order.arrivalDate
        context['order'] = order
        context['items'] = items
        context['shipping'] = shipping
        context['allstatus'] = ORDER_STATUS
        context['dispatcher'] = order.dispatcher
        context['date'] = date
        context['button'] = "Volver a la lista"
        return context


class ChangedispatchView(TemplateView):
    def post(self, request, *args, **kwargs):
        id_dispatch = self.kwargs['pk']
        order = Orders.objects.get(id=id_dispatch)
        new_status = request.POST.get("status")
        update_date = request.POST.get("arrivalDate")
        day = update_date[0:2]
        month = update_date[3:5]
        year = update_date[6:10]
        full_date = year + '-' + month + '-' + day
        update_date = full_date
        order.arrivalDate = update_date
        order.status = new_status
        order.save()
        return redirect(reverse_lazy('dispatch_list'), kwargs={"pk": id_dispatch})


class CreateDispatcher(ValidatorPermissionRequiredMixins, CreateView):
    model = Dispatcher
    form_class = DispatcherForm
    template_name = 'Dispatch/create.html'
    success_url = reverse_lazy('list_dispatcher')
    permission_required = 'add_dispatcher'

    def get_context_data(self, **kwargs):
        context = super(CreateDispatcher, self).get_context_data(**kwargs)
        context['title'] = "Registro de Depachadores"
        context['title2'] = "Registre Un Despachador"
        context['listadoDespacho'] = reverse_lazy('list_dispatcher')
        context['button2'] = "Listado de Despacho"
        context['button'] = "Regitrar Despachador"
        return context


class ListDispacher(ValidatorPermissionRequiredMixins, ListView):
    model = Dispatcher
    template_name = 'Dispatch/list.html'
    permission_required = 'view_dispatcher'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListDispacher, self).get_context_data(**kwargs)
        context['despacher'] = Dispatcher.objects.all()
        context['title'] = "Listado de Depachadores"
        context['title2'] = "Listado de Despachadores en la Base de Datos"
        context['register'] = reverse_lazy('create_dispatcher')
        context['button'] = "Registrar Despachador"
        return context


class UpdateDispatcher(ValidatorPermissionRequiredMixins, UpdateView):
    model = Dispatcher
    form_class = DispatcherForm
    template_name = 'Dispatch/create.html'
    success_url = reverse_lazy('list_dispatcher')
    permission_required = 'change_dispatcher'

    def get_context_data(self, **kwargs):
        context = super(UpdateDispatcher, self).get_context_data(**kwargs)
        context['title'] = "Actualizar al Depachador"
        context['title2'] = "Solicita Actualizar"
        context['listadoDespacho'] = reverse_lazy('list_dispatcher')
        context['button'] = "Actualizar Despachador"
        context['button2'] = "Listado de Despacho"
        return context


class DeleteDispatcher(ValidatorPermissionRequiredMixins, DeleteView):
    model = Dispatcher
    template_name = 'Dispatch/delete.html'
    success_url = reverse_lazy('list_dispatcher')
    permission_required = 'delete_dispatcher'

    def get_context_data(self, **kwargs):
        context = super(DeleteDispatcher, self).get_context_data(**kwargs)
        context['title'] = "Eliminar Despachador"
        context['title2'] = "¿Está seguro que quiere eliminar a "
        context['listadoDespacho'] = reverse_lazy('list_dispatcher')
        return context


class DetailDispatcher(TemplateView):
    model = Dispatcher
    template_name = 'Dispatch/detaildispatcher.html'

    def get_context_data(self, **kwargs):
        context = super(DetailDispatcher, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        dispatcher = Dispatcher.objects.get(pk=pk)
        context['dispatcher'] = dispatcher
        context['button'] = "Volver al Listado"
        context['PDF'] = "Generar PDF"
        return context

















