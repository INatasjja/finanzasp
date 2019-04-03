from django.apps import AppConfig
from watson import search as watson

class FinanzasConfig(AppConfig):
    name = 'finanzas'
    def ready(self):
        Corte = self.get_model("Corte")
        watson.register(Corte)


class YourAppConfig(AppConfig):
    name = 'finanzas'
    def ready(self):
        Corte = self.get_model("Corte")
        watson.register(Corte)