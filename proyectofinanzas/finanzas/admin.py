from django.contrib import admin
from .models import *


class TipoTransaccionAdmin(admin.ModelAdmin):
    list_display = ('Descripcion',)

# Register your models here.
admin.site.register (Users)
admin.site.register (Egreso)
admin.site.register (RenglonEgreso)
admin.site.register (TipoPago)
admin.site.register (Fuente)
admin.site.register (Ingreso)
admin.site.register (Corte)
admin.site.register (GestionEgreso)
admin.site.register (Transacciones)
admin.site.register (TransaccionesCorte)