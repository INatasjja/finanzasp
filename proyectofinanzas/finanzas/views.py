from django.shortcuts import get_object_or_404, render_to_response, redirect, render, reverse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .render import *
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from datetime import datetime
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from easy_pdf.views import PDFTemplateView
from django.views.generic import View
from django.utils import timezone
import csv
from django.db.models import Q
from itertools import chain



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
def adduser(request):
    data = Users.objects.get(username = request.user)
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = CreateForm()

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



@login_required
def create(request):
    data = Users.objects.get(username = request.user)
    if request.method == 'POST':
        form = EditPasswordForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = EditPasswordForm(instance=data)

    context = {'username':request.user,'form':form}
    return render(request, 'finanzas/edits.html', context)



@login_required
def delete(request,tipo,id):

	if tipo == 'e':
		to_delete = get_object_or_404(Egreso,id=id,Usuario = request.user)
		form = DelEgresoForm(request.POST or None, instance = to_delete)
	elif tipo == 'i':
		to_delete = get_object_or_404(Ingreso,id=id,Usuario = request.user)
		form = DelIngresoForm(request.POST or None, instance = to_delete)
	elif tipo == 'r':
		to_delete = get_object_or_404(RenglonEgreso,id=id,Usuario = request.user)
		form = DelRenglonEgresoForm(request.POST or None, instance = to_delete)
	elif tipo == 'p':
		to_delete = get_object_or_404(TipoPago,id=id,Usuario = request.user)
		form = DelTipoPagoForm(request.POST or None, instance = to_delete)
	elif tipo == 't':
		to_delete = get_object_or_404(Transacciones,id=id,Usuario = request.user)
		form = DelTransaccionesForm(request.POST or None, instance = to_delete)
	elif tipo == 'c':
		to_delete = get_object_or_404(Corte,id=id,Usuario = request.user)
		form = DelCorteForm(request.POST or None, instance = to_delete)  


	if request.method == "POST":
		if tipo == 'e':
			to_delete = get_object_or_404(Egreso,id=id,Usuario = request.user)
			form = DelEgresoForm(request.POST or None, instance = to_delete)
			redirect = '/list/{}'.format(tipo)
		elif tipo == 'i':
			to_delete = get_object_or_404(Ingreso,id=id,Usuario = request.user)
			form = DelIngresoForm(request.POST or None, instance = to_delete)
			redirect = '/list/{}'.format(tipo)
		elif tipo == 'r':
			to_delete = get_object_or_404(RenglonEgreso,id=id,Usuario = request.user)
			form = DelRenglonEgresoForm(request.POST or None, instance = to_delete)
			redirect = '/list/{}'.format(tipo)
		elif tipo == 'p':
			to_delete = get_object_or_404(TipoPago,id=id,Usuario = request.user)
			form = DelTipoPagoForm(request.POST or None, instance = to_delete)
			redirect = '/list/{}'.format(tipo)
		elif tipo == 't':
			to_delete = get_object_or_404(Transacciones,id=id,Usuario = request.user)
			form = DelTransaccionesForm(request.POST or None, instance = to_delete)
			redirect = '/transacciones/'
		elif tipo == 'c':
			to_delete = get_object_or_404(Corte,id=id,Usuario = request.user)
			form = DelCorteForm(request.POST or None, instance = to_delete)
			redirect = '/miscortes/'

		if form.is_valid():
			to_delete.EstadoActivo=0
			to_delete.save()
			return HttpResponseRedirect(redirect)
		else:
			if tipo == 'e':
				form = DelEgresoForm(instance = to_delete)
			elif tipo == 'i':
				form = DelIngresoForm(instance = to_delete)
			elif tipo == 'r':
				form = DelRenglonEgresoForm(instance = to_delete)
			elif tipo == 'p':
				form = DelTipoPagoForm(instance = to_delete)
			elif tipo == 't':
    				form = DelTransaccionesForm(instance = to_delete)
			elif tipo == 'c':
    				form = DelCorteForm(instance = to_delete)


	content = {'title_page':'Editar','form':form,'tipo':tipo,'mensajes':f'Borrara el registro con id {to_delete.id}','tmensaje':'alert-danger'}
	return render (request, 'finanzas/edit_tipo.html',content)


@login_required
def updateE(request,id):
    data = Egreso.objects.get(Usuario = request.user,id=id)
    if request.method == 'POST':
        form = EgresoForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/e/')
    else:
        form = EgresoForm(instance=data)

    context = {'username':request.user,'form':form}
    return render(request, 'finanzas/update.html', context)


@login_required
def updateI(request,id):
    data = Ingreso.objects.get(Usuario = request.user,id=id)
    if request.method == 'POST':
        form = IngresoForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/i/')
    else:
        form = IngresoForm(instance=data)

    context = {'username':request.user,'form':form}
    return render(request, 'finanzas/update.html', context)


@login_required
def updateR(request,id):
    data = RenglonEgreso.objects.get(Usuario = request.user,id=id)
    if request.method == 'POST':
        form = RenglonEgresoForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/r/')
    else:
        form = RenglonEgresoForm(instance=data)

    context = {'username':request.user,'form':form}
    return render(request, 'finanzas/update.html', context)

@login_required
def updateP(request,id):
    data = TipoPago.objects.get(Usuario = request.user,id=id)
    if request.method == 'POST':
        form = TipoPagoForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/ti/')
    else:
        form = TipoPagoForm(instance=data)

    context = {'username':request.user,'form':form}
    return render(request, 'finanzas/update.html', context)



def list(request,tipo):
    if tipo == 'p':
    	data = TipoPago.objects.filter(Usuario=request.user)
    	template='finanzas/list_ti.html'
    elif tipo == 'i':
    	data = Ingreso.objects.filter(Usuario=request.user)
    	template='finanzas/list_i.html'

    elif tipo == 'e':
        data = Egreso.objects.filter(Usuario=request.user)
        template='finanzas/list_e.html'	

    elif tipo == 'r':
        data = RenglonEgreso.objects.filter(Usuario=request.user)
        template='finanzas/list_r.html'		

    context = {'username':request,'data':data}
    return render(request, template, context)


def listCorte(request):
    data = Corte.objects.filter(Usuario=request.user, EstadoActivo=1).order_by('-id')
    template='finanzas/list_c.html'		
    context = {'username':request,'data':data}
    return render(request, template, context)


Meses = {'Ene':1,
         'Feb':2,
         'Mar':3,
         'Abr':4,
         'May':5,
         'Jun':6,
         'Jul':7,
         'Ago':8,
         'Sep':9,
         'Oct':10,
         'Nov':11,
         'Dec':12,}



def GenerarCorte (user,Ano,Mes):
    tingreso = 0
    tegreso = 0
    transacciones = []
    ingresos = Transacciones.objects.filter(Usuario=str(user),TipoTransaccion='I',EstadoActivo=1)
    egresos = Transacciones.objects.filter(Usuario=str(user),TipoTransaccion='E',EstadoActivo=1)
    for i in ingresos:
        if i.FechaTransaccion.month == Meses.get(Mes) and i.FechaTransaccion.year == int(Ano):
            tingreso = tingreso + int(i.Monto)
            transacciones.append(i.id)
    for e in egresos:
        if e.FechaTransaccion.month == Meses.get(Mes) and e.FechaTransaccion.year == int(Ano):
            tegreso = tegreso + int(e.Monto)
            transacciones.append(e.id)

    data = {'TotalIngresos':tingreso,'TotalEgresos':tegreso,'BalanceCorte':tingreso - tegreso,'transacciones':transacciones}
    return data



def GeneraCorte(request):
    BalanceInicial = Users.objects.get(username = request.user).limite
    if request.method == 'POST':
        form = GeneraCorteForm(request.POST)
        if form.is_valid():
            DatoCorte = GenerarCorte(request.user.id,request.POST['Ano'],request.POST['Mes'])
            #form.save()
            Corte.objects.create(Usuario=request.user,
                                 Ano=request.POST['Ano'],
                                 Mes=request.POST['Mes'],
                                 FechaCorte = datetime.today(),
                                 BalanceInicial = BalanceInicial,
                                 TotalIngresos = DatoCorte['TotalIngresos'],
                                 TotalEgresos = DatoCorte['TotalEgresos'],
                                 BalanceCorte = DatoCorte['BalanceCorte'],
                                 Comentario=request.POST['Comentario'])
            corteCreado = Corte.objects.latest('id')
            for x in DatoCorte['transacciones']:
                TransaccionesCorte.objects.create(Usuario = request.user,
                                                  Transaccion = Transacciones.objects.get(id=x),
                                                  corte = corteCreado,
                                                  fecha = datetime.today())
            return HttpResponseRedirect('/miscortes/')
    else:
        form = GeneraCorteForm()

    context = {'username':request.user,'form':form}
    return render(request, 'finanzas/list_c_Gen.html', context)


def listCorteDet(request,id):
    general = Corte.objects.get(Usuario=request.user,id=id)
    data = TransaccionesCorte.objects.filter(Usuario=request.user,corte=id)
    template='finanzas/list_c_det.html'		

    context = {'username':request,'data':data,'general':general}
    return render(request, template, context)


@login_required
def createE(request):
    if request.method == 'POST':
        form = EgresoForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/e/')
    else:
        form = EgresoForm()

    context = {'username':request.user,'form':form}
    return render(request, 'finanzas/update.html', context)


@login_required
def createI(request):
    if request.method == 'POST':
        form = IngresoForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/i/')
    else:
        form = IngresoForm()

    context = {'username':request.user,'form':form}
    return render(request, 'finanzas/update.html', context)


@login_required
def createR(request):
    if request.method == 'POST':
        form = RenglonEgresoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/r/')
    else:
        form = RenglonEgresoForm()

    context = {'username':request.user,'form':form}
    return render(request, 'finanzas/update.html', context)

@login_required
def createP(request):
    if request.method == 'POST':
        form = TipoPagoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/ti/')
    else:
        form = TipoPagoForm()

    context = {'username': request.user,'form':form}
    return render(request, 'finanzas/update.html', context)





















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

@login_required
def RegistroIngreso(request):
    if request.method == 'POST':
        form = GeneraCorteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/miscortes/')
    else:
        form = GeneraCorteForm()

    context = {'username':request.user,'form':form}
    return render(request, 'finanzas/list_c_Gen.html', context)

@login_required
def RegistroGasto(request):
    if request.method == 'POST':
        form = GeneraCorteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/miscortes/')
    else:
        form = GeneraCorteForm()

    context = {'username':request.user,'form':form}
    return render(request, 'finanzas/list_c_Gen.html', context)


@login_required
def Transaccione(request):
    data = Transacciones.objects.filter(Usuario=request.user,EstadoActivo=1)
    template = 'finanzas/list_transacciones.html'

    context = {'username':request.user,'data': data}
    return render(request, template, context)

@login_required
def AddTransaccione(request):
    if request.method == 'POST':
        form = TransaccionesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/transacciones/')
    else:
        form = TransaccionesForm()

    context = {'username':request.user,'form':form}
    return render(request, 'finanzas/add_transacciones.html', context)
    
@login_required
def EditTransaccione(request,id):
    data = Transacciones.objects.get(Usuario=request.user,id=id)
    if request.method == 'POST':
        form = TransaccionesForm(request.POST or None, instance = data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/transacciones/')
    else:
        form = TransaccionesForm(instance = data)

    context = {'username':request.user,'form':form}
    return render(request, 'finanzas/add_transacciones.html', context)

def Pdfp(request,id):
    today = timezone.now()
    general = Corte.objects.get(Usuario=request.user,id=id,EstadoActivo=1)
    data = TransaccionesCorte.objects.filter(Usuario=request.user,corte=id,Activo=1)
    context = {
            'today': today,
            'general': general,
            'data': data,
            'request': request
        }
    return render(request, 'html.html', context)


class Pdf(View):
    def get(self, request,id):
        today = timezone.now()
        general = Corte.objects.get(Usuario=request.user,id=id)
        data = TransaccionesCorte.objects.filter(Usuario=request.user,corte=id)
        params = {
            'today': today,
            'general': general,
            'data': data,
            'request': request
        }
        return Render.render('pdf.html', params)


def Csv(request,id):
    general = Corte.objects.get(Usuario=request.user,id=id)
    data = TransaccionesCorte.objects.filter(Usuario=request.user,corte=id)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="corte.csv"'
    writer = csv.writer(response)
    writer.writerow(['usuario','corte','tipo', 'Concepto', 'Monto', 'FechaRegistro','FechaTransaccion'])
    for x in data: writer.writerow([request.user.username,x.corte.id, x.Transaccion.TipoTransaccion, x.Transaccion.Descripcion, x.Transaccion.Monto, x.Transaccion.FechaRegistro,x.Transaccion.FechaTransaccion])
    return response

def Busqueda(request):
    template = 'finanzas/busqueda.html'
    query = request.GET.get('q')
    results = chain(
            Ingreso.objects.filter(Q(Descripcion__icontains=query) | Q(TipoIngreso__icontains=query)), 
            Egreso.objects.filter(Q(Descripcion__icontains=query) | Q(TipoEgreso__icontains=query)),
            Users.objects.filter(Q(username__icontains=query) | Q(cedula__icontains=query)),
            )
            
    
    print(results)
    context = {'items':results}
    return render(request, template, context)