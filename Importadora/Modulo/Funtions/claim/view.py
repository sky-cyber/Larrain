from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, TemplateView
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
        context['title'] = "Soporte"
        context['title2'] = "Coméntanos ¿En qué podemos ayudarte?"
        context['button'] = "Enviar Mensaje"
        return context


class ClaimListView(LoginRequiredMixin, ValidatorPermissionRequiredMixins, TemplateView):
    model = Contact
    template_name = "Claim/list.html"
    permission_required = 'view_contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Reclamos"
        context['title2'] = "Listado"
        context['object_list'] = Contact.objects.filter(typeClaim="Reclamo").order_by("-id")
        return context


class ClaimDeleteView(LoginRequiredMixin, ValidatorPermissionRequiredMixins, DeleteView):
    model = Contact
    template_name = "Claim/delete.html"
    success_url = reverse_lazy('list_claim')
    permission_required = 'delete_contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminación de una Solicitud"
        context['title2'] = "¿Desea eliminar la Solicitud de"
        context['url_claim'] = reverse_lazy('list_claim')
        return context


class QueryList(TemplateView):
    model = Contact
    template_name = 'Claim/listquery.html'

    def get_context_data(self, **kwargs):
        context = super(QueryList, self).get_context_data(**kwargs)
        context['title'] = "Listado de Consultas"
        context['title2'] = "Listado"
        context['object_list'] = Contact.objects.filter(typeClaim="Consulta").order_by("-id")
        return context


class SuggestionList(TemplateView):
    model = Contact
    template_name = 'Claim/suggestionList.html'

    def get_context_data(self, **kwargs):
        context = super(SuggestionList, self).get_context_data(**kwargs)
        context['title'] = "Listado de Sugerencias"
        context['title2'] = "Listado"
        context['object_list'] = Contact.objects.filter(typeClaim="Sugerencía").order_by("-id")
        return context


class CongratulationList(TemplateView):
    model = Contact
    template_name = 'Claim/congratulationList.html'

    def get_context_data(self, **kwargs):
        context = super(CongratulationList, self).get_context_data(**kwargs)
        context['title'] = "Listado de Felicitaciones"
        context['title2'] = "Listado"
        context['object_list'] = Contact.objects.filter(typeClaim="Felicitaciones").order_by("-id")
        return context


