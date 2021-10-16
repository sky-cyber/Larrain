
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from Modulo.Funtions.claim.form import ClaimForm
from PuntoVentas.models import Contact


class ContactCreateView(CreateView):
    model = Contact
    template_name = "Web/contact.html"
    form_class = ClaimForm
    success_url = reverse_lazy('contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Contactanos"
        context['title2'] = "Comentanos ¿En que podemos ayudarte?"
        context['button'] = "Enviar Mensaje"
        return context


class ClaimListView(ListView):
    model = Contact
    template_name = "Claim/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado De Reclamos o Opiniones"
        context['title2'] = "Listado"
        context['object_list'] = Contact.objects.all()
        return context


class ClaimDeleteView(DeleteView):
    model = Contact
    template_name = "Claim/delete.html"
    success_url = reverse_lazy('claim_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminación de un Reclamo"
        context['title2'] = "¿Desea eliminar el Reclamo de"
        context['url_claim'] = reverse_lazy('claim_list')
        return context