from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from Modulo.Funtions.claim.form import ClaimForm
from PuntoVentas.models import Contact
from PuntoVentas.mixins import ValidatorPermissionRequiredMixins


class ContactCreateView(CreateView):
    model = Contact
    template_name = "Web/contact.html"
    form_class = ClaimForm
    success_url = reverse_lazy('contact')
    permission_required = 'add_contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Contactanos"
        context['title2'] = "Coméntanos ¿En qué podemos ayudarte?"
        context['button'] = "Enviar Mensaje"
        return context


class ClaimListView(LoginRequiredMixin, ValidatorPermissionRequiredMixins, ListView):
    model = Contact
    template_name = "Claim/list.html"
    permission_required = 'view_contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado De Reclamos u Opiniones"
        context['title2'] = "Listado"
        context['object_list'] = Contact.objects.all()
        return context


class ClaimDeleteView(LoginRequiredMixin, ValidatorPermissionRequiredMixins, DeleteView):
    model = Contact
    template_name = "Claim/delete.html"
    success_url = reverse_lazy('claim_list')
    permission_required = 'delete_contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminación de un Reclamo"
        context['title2'] = "¿Desea eliminar el Reclamo de"
        context['url_claim'] = reverse_lazy('claim_list')
        return context