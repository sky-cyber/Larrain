from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from PuntoVentas.models import Client, Sale
from Modulo.Funtions.Sales.form import ClientForm, SaleForm
from PuntoVentas.mixins import ValidatorPermissionRequiredMixins


class CreateClient(ValidatorPermissionRequiredMixins, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'Sales/create.html'
    success_url = reverse_lazy('list_client_face')
    permission_required = 'add_client'

    def get_context_data(self, **kwargs):
        context = super(CreateClient, self).get_context_data(**kwargs)
        context['title'] = "Generar Registros de Clientes Desde Las Sucursales"
        context['title2'] = "Registre un Cliente"
        context['button'] = "Registrar Nuevo Cliente"
        context['button2'] = "Listado de Clientes"
        context['listClient'] = reverse_lazy('list_client_face')
        return context


class ListClientFaceToFace(ValidatorPermissionRequiredMixins, ListView):
    model = Client
    template_name = 'Sales/list.html'
    permission_required = 'view_client'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListClientFaceToFace, self).get_context_data(**kwargs)
        context['clienteFace'] = Client.objects.all()
        context['title'] = "Listado de Clientes Registrados En Sucursal"
        context['title2'] = "Listado de Clientes Que Son Registrados Por Los Vendedores"
        context['registerClient'] = reverse_lazy('create_client')
        context['button'] = "Nuevo Cliente"
        return context


class UpdateClient(ValidatorPermissionRequiredMixins, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'Sales/create.html'
    success_url = reverse_lazy('list_client_face')
    permission_required = 'change_client'

    def get_context_data(self, **kwargs):
        context = super(UpdateClient, self).get_context_data(**kwargs)
        context['title'] = "Actualización de un Cliente"
        context['title2'] = "Editar al cliente"
        context['listClient'] = reverse_lazy('list_client_face')
        context['button'] = "Editar Cliente"
        context['button2'] = "Listado de Clientes"
        return context


class DeleteClient(ValidatorPermissionRequiredMixins, DeleteView):
    model = Client
    template_name = 'Sales/delete.html'
    success_url = reverse_lazy('list_client_face')
    permission_required = 'delete_client'

    def get_context_data(self, **kwargs):
        context = super(DeleteClient, self).get_context_data(**kwargs)
        context['title'] = "Eliminación de un Cliente"
        context['title2'] = "¿Quiere eliminar a  "
        context['listClient'] = reverse_lazy('list_client_face')
        return context


class DetailClientOffice(TemplateView):
    model = Client
    template_name = 'Sales/detail_client_office.html'

    def get_context_data(self, **kwargs):
        context = super(DetailClientOffice, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        client = Client.objects.get(pk=pk)
        context['client'] = client
        return context


class SaleClient(CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'Sales/createSale.html'
    success_url = reverse_lazy('adm')

    def get_context_data(self, **kwargs):
        context = super(SaleClient, self).get_context_data(**kwargs)
        context['title'] = "Crear Un Pedido"
        context['title2'] = "Detalle del Producto"
        context['title3'] = "Datos De La Orden"
        return context




















