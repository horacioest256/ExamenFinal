from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def ingresoUsuario(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        contraUsuario = request.POST.get('contraUsuario')
        usrObj = authenticate(request,username=nombreUsuario, password=contraUsuario)
        if usrObj is not None:
            login(request,usrObj)
            return HttpResponseRedirect(reverse('app4:informacionUsuario'))
        else:
            return HttpResponseRedirect(reverse('app4:ingresoUsuario'))
    return render(request,'ingresoUsuario.html')

@login_required(login_url='/')
def informacionUsuario(request):
    return render(request,'informacionUsuario.html')

@login_required(login_url='/')
def cerrarSesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('app4:ingresoUsuario'))

def ejemploJs(request):
    return render(request,'ejemploJs.html')