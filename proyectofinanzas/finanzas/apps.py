from django.apps import AppConfig

class FinanzasConfig(AppConfig):
    name = 'finanzas'
    def ready(self):
        Corte = self.get_model("Corte")


class YourAppConfig(AppConfig):
    name = 'finanzas'
    def ready(self):
        Corte = self.get_model("Corte")
