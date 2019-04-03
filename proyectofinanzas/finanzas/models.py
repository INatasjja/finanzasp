from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser,User
from django.conf import settings
import datetime



# Create your models here.


class Users(AbstractUser):
    cedula = models.CharField(max_length=13, blank=True)
    tipoPersona = models.CharField(max_length=3, choices=(('F', 'Fisica'), ('J', 'Juridica')),default='F')
    limite = models.IntegerField(default=0)


class Egreso(models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID  de Egreso')
    Usuario=models.ForeignKey (Users, on_delete=models.CASCADE, default=1)
    TipoEgreso=models.CharField (max_length=50, help_text='Tipo de egreso')
    Descripcion= models.CharField (max_length=50, help_text='Descripcion')
    EstadoActivo=models.BooleanField (default=1)

    def __str__(self):
        return self.TipoEgreso


class RenglonEgreso (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Gestion de Ingreso')
    Usuario=models.ForeignKey (Users, on_delete=models.CASCADE, default=1)
    Nombre=models.CharField (max_length=50, help_text='Tipo de ingreso')
    Descripcion= models.CharField (max_length=50, help_text='Descripcion')
    Institucion=models.CharField(max_length=35, help_text='Institucion, empleador o cliente')
    EstadoActivo=models.BooleanField (default=1)

    def __str__(self):
        return self.Nombre

class TipoPago (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Gestion de Ingreso')
    Usuario=models.ForeignKey (Users, on_delete=models.CASCADE, default=1)
    Descripcion=models.CharField (max_length=50, help_text='Tipo de de pago (Tarjeta, efectivo, etc).')
    EstadoActivo=models.BooleanField (default=1)

    def __str__(self):
        return self.Descripcion

class Fuente (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Gestion de Ingreso')
    Usuario=models.ForeignKey (Users, on_delete=models.CASCADE, default=1)
    Descripcion=models.CharField (max_length=50, help_text='Fuente Ingreso')
    Institucion=models.CharField(max_length=35)
    EstadoActivo=models.BooleanField (default=1)

    def __str__(self):
        return self.Descripcion

class Ingreso (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID de Ingreso')
    Usuario=models.ForeignKey (Users, on_delete=models.CASCADE, default=1)
    TipoIngreso=models.CharField (max_length=50, help_text='Tipo de ingreso')
    Fuente= models.ForeignKey(Fuente, on_delete=models.CASCADE)
    Descripcion= models.CharField (max_length=50, help_text='Descripcion')
    EstadoActivo=models.BooleanField (default=1)

    def __str__(self):
        return self.TipoIngreso

class GestionEgreso (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Gestion de Ingreso')
    Usuario=models.ForeignKey (Users, on_delete=models.CASCADE, default=1)
    TipoIngreso=models.ForeignKey (Egreso, on_delete=models.CASCADE)
    Renglon=models.ForeignKey (RenglonEgreso, on_delete=models.CASCADE)
    TipoPago=models.ForeignKey (TipoPago, on_delete=models.CASCADE)
    Descripcion= models.CharField (max_length=50, help_text='Descripcion')
    EstadoActivo=models.BooleanField (default=1)

    def __str__(self):
        return self.Descripcion


class Transacciones (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Transaccion')
    Usuario=models.ForeignKey (Users, on_delete=models.CASCADE, default=1)
    TipoTransaccion=models.CharField(max_length=1, choices=(('I', 'Ingreso'), ('E', 'Egreso')),default='')
    FechaTransaccion=models.DateField(default=datetime.date.today)
    FechaRegistro=models.DateField (auto_now=True)
    Monto=models.CharField (max_length=12, help_text='Monto Transaccion')
    Descripcion= models.CharField (max_length=50, help_text='Descripcion')
    EstadoActivo=models.BooleanField (default=1)

    def __str__(self):
        return self.Descripcion

class Corte (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Corte')
    Usuario=models.ForeignKey (Users, on_delete=models.CASCADE, default=1)
    Ano=models.IntegerField (validators=[MinValueValidator(2000)], default=2019, help_text='Ano')
    Mes=models.CharField(max_length=3, choices=(('Ene', 'Enero'), ('Feb', 'Febrero'),('Mar', 'Marzo'), ('Abr', 'Abril'),
    ('May', 'Mayo'), ('Jun', 'Junio'),('Jul', 'Julio'), ('Ago', 'Agosto'),('Sep', 'Septiembre'), ('Oct', 'Octubre'),
    ('Nov', 'Noviembre'), ('Dic', 'Diciembre')),default='')
    FechaCorte=models.DateField(auto_now=True)
    BalanceInicial=models.IntegerField (default=0)
    TotalIngresos=models.IntegerField (default=0)
    TotalEgresos=models.IntegerField (default=0)
    BalanceCorte=models.IntegerField (default=0)
    Comentario=models.TextField(default='')
    EstadoActivo=models.BooleanField (default=1)
    

    def __str__(self):
        return '{} {}'.format(self.Mes,self.id)

    
class TransaccionesCorte (models.Model):
    id = models.AutoField (primary_key=True, help_text= 'ID Transaccion')
    Usuario=models.ForeignKey (Users, on_delete=models.CASCADE, default=1)
    Transaccion = models.ForeignKey(Transacciones, on_delete=models.CASCADE, default=1)
    Activo=models.BooleanField (default=1)
    corte = models.ForeignKey (Corte,on_delete=models.CASCADE, default=0)
    fecha = models.DateField (default=datetime.date.today)

    def __str__(self):
        return self.Transaccion.Descripcion