from django.apps import AppConfig


class CarConfig(AppConfig):
    name = "apps.cars"

    def ready(self):
        from . import signals
