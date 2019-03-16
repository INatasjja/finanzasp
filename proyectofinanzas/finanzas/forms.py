from django import forms
from django.forms import ModelForm, Textarea
from .models import *
from .validators import valida_cedula


#class EditForm(forms.ModelForm):
#	class Meta:
#		model = TipoTransaccion
#		fields = ('Descripcion','Activo','Tipo')
#
#		
#class DelForm(forms.ModelForm):
#	class Meta:
#		model = TipoTransaccion
#		fields = ()

class EditForm (ModelForm):
    cedula = forms.CharField(max_length=13,validators=[valida_cedula] )
    
    class Meta:
        model = Users
        fields = ['username','cedula','email','limite','tipoPersona']

        widgets = {
            'password' : forms.PasswordInput(),
        }


class EditPasswordForm (ModelForm):
        
    class Meta:
        model = Users
        fields = ['password',]

        widgets = {
            'password' : forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super(EditPasswordForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class TipoPagoForm(ModelForm):

	class Meta:
		model = TipoPago
		fields = ['Nombre','EstadoActivo',]


class IngresoForm(ModelForm):
    
	class Meta:
		model = Ingreso
		fields = ['TipoIngreso','Fuente','Descripcion','EstadoActivo',]


class EgresoForm(ModelForm):
    
	class Meta:
		model = Egreso
		fields = ['TipoEgreso','Descripcion','EstadoActivo',]



class RenglonEgresoForm(ModelForm):
    
	class Meta:
		model = RenglonEgreso
		fields = ['Nombre','Descripcion','Institucion','EstadoActivo',]