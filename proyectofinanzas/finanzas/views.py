from django.shortcuts import get_object_or_404, render_to_response, redirect, render, reverse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import TipoTransaccion
from .forms import EditForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def project_list (request):
	return render (request, 'finanzas/project_list.html')

def project_detail (request, project_slug):
	#fetch the corrrect project
	return render (request, 'finanzas/project_detail.html')


@login_required(login_url='login/')
def index (request):
	content = {'title_page':'Inicio'}
	return render (request, 'finanzas/index.html',content)

@login_required(login_url='login/')
def tipo_detail(request,tipo_id):
	data = TipoTransaccion.objects.all().filter(Tipo=tipo_id.upper())
	print(data)
	content = {'title_page':'Listado','datos':data}
	return render (request, 'finanzas/tipo_detail.html',content)

@login_required(login_url='login/')
def TipoTransaccionEdit(request,tipo,id):
	data = TipoTransaccion.objects.filter(id=id).values()[0]
	form = EditForm(initial={'Descripcion':data.get('Descripcion'),
	                              'Activo':data.get('Activo'),
								    'Tipo':data.get('Tipo'),})
	if request.method == "POST":
		form = EditForm(request.POST)
		if form.is_valid():
			Descripcion = form.cleaned_data['Descripcion']
			Activo = form.cleaned_data['Activo']
			Tipo = form.cleaned_data['Tipo']
			TipoTransaccion.objects.get_or_create(Descripcion=Descripcion,Activo=Activo,Tipo=Tipo)
			return HttpResponseRedirect('/list/{}'.format(tipo))
		else:
			form = EditForm()
	content = {'title_page':'Editar','form':form}
	return render (request, 'finanzas/edit_tipo.html',content)



def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your account was inactive.")
		else:
			return HttpResponse("Invalid login details given")
		return HttpResponseRedirect(reverse('index'))
	else:
		return render(request, 'finanzas/login.html', {})
		context = {'': ''}
	return render(request, 'finanzas/login.html', context)



@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))