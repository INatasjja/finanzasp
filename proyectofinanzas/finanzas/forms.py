from django import forms
from django.forms import ModelForm, Textarea
from .models import *


class EditForm(forms.ModelForm):
	class Meta:
		model = TipoTransaccion
		fields = ('Descripcion','Activo','Tipo')
		#Descripcion= forms.CharField(max_length=15,label='Descripcion',widget= forms.TextInput(attrs={'class':'form-control','id':'exampleInputName1','placeholder':'Descripcion'}))
		#Activo= forms.BooleanField(required=False)
		#Tipo= forms.ChoiceField(choices=(('I', 'Ingresos'), ('E', 'Egresos'), ('R', 'Renglones de Egresos'), ('P','Tipos de Pagos')),required=True)
		
		
class DelForm(forms.ModelForm):
	class Meta:
		model = TipoTransaccion
		fields = ()


class RegisterForm(forms.ModelForm):
	class Meta:
		model = settings.AUTH_USER_MODEL
		fields = ('',)