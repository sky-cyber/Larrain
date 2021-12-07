from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from PuntoVentas.models import FlatFile
from Modulo.Funtions.File.form import FileForm
from PuntoVentas.mixins import ValidatorPermissionRequiredMixins


class FileUpload(LoginRequiredMixin, ValidatorPermissionRequiredMixins, CreateView):
    model = FlatFile
    form_class = FileForm
    template_name = 'File/create.html'
    success_url = reverse_lazy('file_list')
    permission_required = 'add_flatfile'

    def get_context_data(self, **kwargs):
        context = super(FileUpload, self).get_context_data(**kwargs)
        context['button'] = "Registrar Lista"
        context['filelist'] = reverse_lazy('file_list')
        context['button2'] = "Volver Al Listado"
        context['title'] = "Subir Un Archivo"
        context['title2'] = "Registro"
        return context


class FileList(LoginRequiredMixin, ValidatorPermissionRequiredMixins, ListView):
    model = FlatFile
    template_name = 'File/list.html'
    permission_required = 'view_flatfile'

    def get_context_data(self, **kwargs):
        context = super(FileList, self).get_context_data(**kwargs)
        context['upload'] = reverse_lazy('file_upload')
        context['button'] = "Subir Archivo"
        context['title'] = "Listado De Archivos"
        context['title2'] = "Listado"
        return context


class FileUpdate(LoginRequiredMixin, ValidatorPermissionRequiredMixins, UpdateView):
    model = FlatFile
    form_class = FileForm
    template_name = 'File/create.html'
    success_url = reverse_lazy('file_list')
    permission_required = 'change_flatfile'

    def get_context_data(self, **kwargs):
        context = super(FileUpdate, self).get_context_data(**kwargs)
        context['button'] = "Editar Archivo"
        context['filelist'] = reverse_lazy('file_list')
        context['button2'] = "Volver Al Listado"
        context['title'] = "Actualización de Archivo Plano"
        context['title2'] = "Actualización"
        return context


class FileDelete(LoginRequiredMixin, ValidatorPermissionRequiredMixins, DeleteView):
    model = FlatFile
    template_name = 'File/delete.html'
    success_url = reverse_lazy('file_list')
    permission_required = 'delete_flatfile'

    def get_context_data(self, **kwargs):
        context = super(FileDelete, self).get_context_data(**kwargs)
        context['title'] = "Eliminación de un Archivo Plano"
        context['title2'] = "¿Quiere eliminar El Archivo "
        context['url_list'] = reverse_lazy('file_list')
        return context
