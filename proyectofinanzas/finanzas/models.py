from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser,User
from django.conf import settings


# Create your models here.


class Egreso (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID  de Egreso')
    TipoEgreso=models.CharField (max_length=50, help_text='Tipo de egreso')
    Descripcion= models.CharField (max_length=50, help_text='Descripcion')
    EstadoActivo=models.BooleanField (default=1)

    def __str__(self):
        return str(self.TipoEgreso)


class RenglonEgreso (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Gestion de Ingreso')
    Nombre=models.CharField (max_length=50, help_text='Tipo de ingreso')
    Descripcion= models.CharField (max_length=50, help_text='Descripcion')
    Institucion=models.CharField(max_length=35, help_text='Institucion, empleador o cliente')
    EstadoActivo=models.BooleanField (default=1)

    def __str__(self):
        return str(self.Nombre)

class TipoPago (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Gestion de Ingreso')
    Nombre=models.CharField (max_length=50, help_text='Tipo de de pago (Tarjeta, efectivo, etc).')
    EstadoActivo=models.BooleanField (default=1)

    def __str__(self):
        return str(self.Nombre)

class Fuente (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Gestion de Ingreso')
    Nombre=models.CharField (max_length=50, help_text='Fuente Ingreso')
    Institucion=models.CharField(max_length=35)
    EstadoActivo=models.BooleanField (default=1)

    def __str__(self):
        return str(self.Nombre)

class Ingreso (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID de Ingreso')
    TipoIngreso=models.CharField (max_length=50, help_text='Tipo de ingreso')
    Fuente=models.ForeignKey(Fuente)
    Descripcion= models.CharField (max_length=50, help_text='Descripcion')
    EstadoActivo=models.BooleanField (default=1)

    def __str__(self):
        return str(self.TipoIngreso)

class GestionEgreso (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Gestion de Ingreso')
    TipoIngreso=models.ForeignKey (TipoEgreso)
    Renglon=models.ForeignKey (RenglonEgreso)
    TipoPago=models.ForeignKey (TipoPago)
    Descripcion= models.CharField (max_length=50, help_text='Descripcion')
    EstadoActivo=models.BooleanField (default=1)

    def __str__(self):
        return str(self.Descripcion)


class Transacciones (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Transaccion')
    Usuario=models.ForeignKey (Users, on_delete=None)
    TipoTransaccion=models.CharField(max_length=1, choices=(('I', 'Ingreso'), ('E', 'Egreso')),default='')
    FechaTransaccion=models.DateField
    FechaRegistro=models.DateField (auto_now=True)
    Monto=models.CharField (max_length=12, help_text='Monto Transaccion')
    Descripcion= models.CharField (max_length=50, help_text='Descripcion')
    EstadoActivo=models.BooleanField (default=1)

    def __str__(self):
        return str(self.Descripcion)

class Corte (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Corte')
    Usuario=models.ForeignKey (Users, on_delete=None, default='')
    Ano=models.IntegerField (validators=[MinValueValidator(2000)], default=2019, help_text='Ano')
    Mes=models.CharField(max_length=3, choices=(('Ene', 'Enero'), ('Feb', 'Febrero'),('Mar', 'Marzo'), ('Abr', 'Abril'),
    ('May', 'Mayo'), ('Jun', 'Junio'),('Jul', 'Julio'), ('Ago', 'Agosto'),('Sep', 'Septiembre'), ('Oct', 'Octubre'),
    ('Nov', 'Noviembre'), ('Dic', 'Diciembre')),default='')
    FechaCorte=models.DateField(auto_now=True)
    BalanceInicial=models.IntegerField (default=0)
    TotalIngresos=models.IntegerField (default=0)
    TotalEgresos=models.IntegerField (default=0)
    BalanceCorte=models.IntegerField (default=0)
    Comentario=models.CharField(Max_lenght=40)
    EstadoActivo=models.BooleanField (default=1)
    

    def __str__(self):
        return str(self.Mes)