from django.views.generic import TemplateView


class WelcomeView(TemplateView):
    template_name = 'Email/welcome.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'correo electronico'
        return context

