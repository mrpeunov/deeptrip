from django.apps import AppConfig


class ToursConfig(AppConfig):
    name = 'tours'
    verbose_name = 'Экскурсии'

    def ready(self):
        import tours.signals.handlers
