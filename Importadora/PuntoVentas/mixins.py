from django.contrib import messages
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from crum import get_current_request

from PuntoVentas.models import *


class ValidatorPermissionRequiredMixins(object):
    permission_required = ''
    url_redirect = None

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('adm')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        request = get_current_request()
        print(request)
        if 'group' in request.session:
            group = request.session['group']
            #group = Group.objects.get(pk=1)
            if group.permissions.filter(codename=self.permission_required):
                return super(ValidatorPermissionRequiredMixins, self).dispatch(request, *args, **kwargs)
            messages.error(request, 'No tiene permiso para ingresar a este modulo')
            return HttpResponseRedirect(self.get_url_redirect())


