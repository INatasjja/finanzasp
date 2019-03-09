from django.contrib import admin
from .models import *


class TipoTransaccionAdmin(admin.ModelAdmin):
    list_display = ('Descripcion',)

# Register your models here.
admin.site.register (TipoTransaccion,TipoTransaccionAdmin)
admin.site.register (GestionEgresos)
admin.site.register (GestionIngresos)
admin.site.register (GestionUsuarios)
admin.site.register (Transacciones)
admin.site.register (Corte)
admin.site.register(Users)