from django.shortcuts import get_object_or_404, render_to_response, redirect, render, reverse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.conf import settings


# Create your views here.
#def Register(request):
#	data = settings.AUTH_USER_MODEL.objects.get(request.pk)
#	form = RegisterForm(request.POST or None, instance=data)
#	if request.method == "POST":
#		form = RegisterForm(request.POST or None)
#		if form.is_valid():
#			form.save()
#			return HttpResponseRedirect('/list/{}'.format(tipo))
#		else:
#			form = RegisterForm()
#	content = {'title_page':'Editar','form':form,'tipo':tipo,'mensajes':f'Añadir Nuevo','tmensaje':'alert-success'}
#	return render (request, 'finanzas/edit_tipo.html',content)



@login_required
def profile(request):
    data = Users.objects.get(username = request.user)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = EditForm(instance=data)

    context = {'username':request.user,'form':form}
    return render(request, 'finanzas\profile.html', context)

@login_required
def profileedit(request):
    data = Users.objects.get(username = request.user)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = EditForm(instance=data)

    context = {'username':request.user,'form':form}
    return render(request, 'finanzas/edit.html', context)


@login_required
def editPassword(request):
    data = Users.objects.get(username = request.user)
    if request.method == 'POST':
        form = EditPasswordForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = EditPasswordForm(instance=data)

    context = {'username':request.user,'form':form}
    return render(request, 'finanzas/edit.html', context)


























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
	content = {'title_page':'Listado','datos':data,'tipo':tipo_id}
	return render (request, 'finanzas/tipo_detail.html',content)

@login_required(login_url='login/')
def TipoTransaccionEdit(request,tipo,id):
	data = TipoTransaccion.objects.get(id=id)
	form = EditForm(request.POST or None, instance=data)
	if request.method == "POST":
		form = EditForm(request.POST or None, instance=data)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/list/{}'.format(tipo))
		else:
			form = EditForm()
	content = {'title_page':'Editar','form':form}
	return render (request, 'finanzas/edit_tipo.html',content)

	
@login_required(login_url='login/')
def TipoTransaccionAdd(request,tipo):
	form = EditForm(request.POST or None)
	if request.method == "POST":
		form = EditForm(request.POST or None)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/list/{}'.format(tipo))
		else:
			form = EditForm()
	content = {'title_page':'Editar','form':form,'tipo':tipo,'mensajes':f'Añadir Nuevo','tmensaje':'alert-success'}
	return render (request, 'finanzas/edit_tipo.html',content)

	
	
def TipoTransaccionDel(request,id):
	to_delete = get_object_or_404(TipoTransaccion,id=id)
	form = DelForm()
	if request.method == "POST":
		form = DelForm(request.POST or None, instance = to_delete)
		if form.is_valid():
			to_delete.delete()
			return HttpResponseRedirect('/list/{}'.format(to_delete.Tipo))
		else:
			form = DelForm(instance = to_delete)
	content = {'title_page':'Editar','form':form,'tipo':to_delete.Tipo,'mensajes':f'Borrara el registro con id {to_delete.id}, {to_delete.Descripcion}','tmensaje':'alert-danger'}
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
				return render(request, 'finanzas/login.html', {'mensaje':'Tu cuenta esta inactiva'})
		else:
			return render(request, 'finanzas/login.html', {'mensaje':'Usuario o Password Incorrectos'})
		return HttpResponseRedirect(reverse('index'))
	else:
		return render(request, 'finanzas/login.html', {'mensaje':'Bienvenido'})
	return render(request, 'finanzas/login.html', {'mensaje':'Bienvenido'})



@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))