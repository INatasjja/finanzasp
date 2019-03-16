from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser,User
from django.conf import settings


# Create your models here.
class TipoTransaccion (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Tipo de Transaccion')
    Descripcion= models.CharField (max_length=50, help_text='Descripcion')
    Activo=models.BooleanField (default=1)
    Tipo=models.CharField(max_length=1, choices=(('I', 'Ingresos'), ('E', 'Egresos'), ('R', 'Renglones de Egresos'), ('P','Tipos de Pagos')),default='')

    def __str__(self):
        return str(self.Descripcion)


class GestionEgresos (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Gestion de Egreso')
    TipoEgreso=models.CharField (max_length=50, help_text='Tipo de egreso')
    RenglonEgreso=models.CharField (max_length=50, help_text='Renglon de egreso')
    TipoPagoxDefecto=models.CharField (max_length=50, help_text='Forma De Pago')
    Descripcion= models.CharField (max_length=50, help_text='Descripcion')
    EstadoActivo=models.BooleanField (default=1)

    def __str__(self):
        return str(self.Descripcion)

class GestionIngresos (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Gestion de Ingreso')
    TipoIngreso=models.CharField (max_length=50, help_text='Tipo de ingreso')
    Origen=models.CharField (max_length=50, help_text='Institucion/Cliente/Empleador')
    Descripcion= models.CharField (max_length=50, help_text='Descripcion')
    EstadoActivo=models.BooleanField (default=1)

    def __str__(self):
        return str(self.Descripcion)

class GestionUsuarios (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Usuario')
    Nombre=models.CharField (max_length=50, help_text='Nombre de Usuario')
    Cedula=models.CharField (max_length=50, help_text='Cedula')
    Limite= models.CharField (max_length=50, help_text='Limite de Egresos del Periodo')
    TipoPersona=models.CharField(max_length=1, choices=(('F', 'Fisica'), ('J', 'Juridica')),default='')
    FechaCorte=models.DateField
    EstadoActivo=models.BooleanField (default=1)

    def __str__(self):
        return str(self.Nombre)

class Transacciones (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Transaccion')
    Usuario=models.ForeignKey (GestionUsuarios, on_delete=None)
    TipoTransaccion=models.CharField(max_length=1, choices=(('I', 'Ingreso'), ('E', 'Egreso')),default='')
    TipoPago=models.CharField(max_length=1, choices=(('T', 'Tarjeta de Credito'), ('E', 'Efectivo'), ('C', 'Cheque')),default='')
    FechaTransaccion=models.DateField
    FechaRegistro=models.DateField (auto_now=True)
    Monto=models.CharField (max_length=12, help_text='Monto Transaccion')
    Descripcion= models.CharField (max_length=50, help_text='Descripcion')
    EstadoActivo=models.BooleanField (default=1)

    def __str__(self):
        return str(self.Descripcion)

class Corte (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Corte')
    Usuario=models.ForeignKey (GestionUsuarios, on_delete=None, default='')
    Ano=models.IntegerField (validators=[MinValueValidator(2000)], default=2019, help_text='Ano')
    Mes=models.CharField(max_length=3, choices=(('Ene', 'Enero'), ('Feb', 'Febrero'),('Mar', 'Marzo'), ('Abr', 'Abril'),
    ('May', 'Mayo'), ('Jun', 'Junio'),('Jul', 'Julio'), ('Ago', 'Agosto'),('Sep', 'Septiembre'), ('Oct', 'Octubre'),
    ('Nov', 'Noviembre'), ('Dic', 'Diciembre')),default='')
    FechaCorte=models.DateField(auto_now=True)
    BalanceInicial=models.IntegerField (default=0)
    TotalIngresos=models.IntegerField (default=0)
    TotalEgresos=models.IntegerField (default=0)
    BalanceCorte=models.IntegerField (default=0)
    

    def __str__(self):
        return str(self.Mes)


#class Users(AbstractUser):
 #   cedula = models.TextField(max_length=11, blank=True)
  #  location = models.CharField(max_length=30, blank=True)
   # birth_date = models.DateField(null=True, blank=True)