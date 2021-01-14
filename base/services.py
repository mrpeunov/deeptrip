from django.views.generic import TemplateView


def _get_menu():
    return {"пример": "20 см"}


def _get_config():
    return {"пример": "25 см"}


def _get_social_networks():
    return {"пример": "15 см"}


class FooterAndMenuTemplateView(TemplateView):
    http_method_names = ['get']

    def add_in_context(self, context):
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.add_in_context(context)
        context.update(_get_menu())
        context.update(_get_config())
        context.update(_get_social_networks())
        return context
