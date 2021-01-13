from django.views.generic import TemplateView


def _get_menu():
    return {"пример": "20 см"}


def _get_config():
    return {"пример": "25 см"}


def _get_social_networks():
    return {"пример": "15 см"}


class FooterAndMenuTemplateView(TemplateView):
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(_get_menu())
        context.update(_get_config())
        context.update(_get_social_networks())
        return context
