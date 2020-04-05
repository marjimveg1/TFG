# -*- coding: utf-8 -*-
from builtins import print

from django.http import HttpResponse

from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from datetime import date, timedelta
from .models import *
from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, 'inicio.html', {"inicioview": True})

def miPerfil(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'miPerfil.html', {"user": user})


def borrarUsuario(request):
    User = get_user_model()
    user = request.user
    if request.method == "POST":
        user.delete()
        return redirect("../../inicio")
    else:

        context = {
            "User": user
        }
        return render(request, 'borrarUsuario.html', context)


def editarPerfil(request):
    User = get_user_model()
    user = request.user

    if request.method == 'GET':
        form = EditarPerfilForm(instance=user)
    else:
        form = EditarPerfilForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return render(request, 'miPerfil.html', {"user": user})
        else:
            form = form

    return render(request, 'editarPerfil.html', {'form': form})


def cambiar_contra(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('cambiarContra')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'cambiarContra.html', {
        'form': form
    })


# REGISTRO DE USUARIOS
def registro(request):
    user = request.user
    if request.method == 'POST':
        form = MamaCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('../inicioSesion')
        else:
            form = form
    else:
        form = MamaCreateForm()
    return render(request, 'registro.html', {'form': form})


# CALENDARIO
def buscarFecha(request):
    return render(request, 'buscarFecha.html')


def crearFechaCalendario(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = FechaCalendarioForm(request.POST)
            if form.is_valid():
                calendario = Calendario.objects.filter(user=user)[0]
                obj = form.save(commit=False)
                obj.calendario = calendario
                form.save()
                return redirect('/miAgenda/')
        else:
            form = FechaCalendarioForm()

    return render(request, 'anadirFechaCalendario.html', {'form': form})





def agenda(request):
    dic_solicitud = request.GET.dict()

    detalle, fecha = getValores(dic_solicitud)

   # fecha = "-90"

    user = request.user
    calendario_owner = Calendario.objects.filter(user=user)[0]
    eventos_owner_lista = Evento.objects.filter(calendario=calendario_owner)
    hoy = date.today()
    getDetalle = False
    getMes= False

    if (detalle=="" and fecha==""): #Quiero ver el mes actual, sin detalles
        year = hoy.year
        month = hoy.month
        fecha_pedida = hoy

    elif(detalle=="" and fecha!=""): #Quiero ver el mes siguiente o el anterior
        fecha_pedida = date(int(fecha[0:4]), int(fecha[5:7]), 1)
        month = fecha_pedida.month
        year = fecha_pedida.year
        getMes = True

    elif(detalle !="" and fecha==""): #Detalle de la fecha detalle en el mes actual
        year = hoy.year
        month = hoy.month
        fecha_pedida = hoy

        if (len(detalle) == 8):
            ano_parametro = detalle[0:4]
            mes_parametro = detalle[4:6]
            dia_parametro = detalle[6:8]

            try:
                nueva_fecha = date(int(ano_parametro), int(mes_parametro), int(dia_parametro))
                getDetalle = True

            except:
                detalles = ""


    else: #Detalle de la fecha detalle en el mes siguiente o anteerior
        fecha_pedida = date(int(fecha[0:4]), int(fecha[5:7]), 1)
        month = fecha_pedida.month
        year = fecha_pedida.year
        getMes = True

        if (len(detalle) == 8):
            ano_parametro = detalle[0:4]
            mes_parametro = detalle[4:6]
            dia_parametro = detalle[6:8]

            try:
                nueva_fecha = date(int(ano_parametro), int(mes_parametro), int(dia_parametro))
                getDetalle = True

            except:
                getDetalle = False


    primer_dia_mes = date(year, month, 1)

    if (month == 12):
        year += 1
        month = 1
    else:
        month += 1
    ultimo_dia_mes = date(year, month, 1) - timedelta(1)
    primer_dia_calendario = primer_dia_mes - timedelta(primer_dia_mes.weekday())
    ultimo_dia_calendario = ultimo_dia_mes + timedelta(7 - ultimo_dia_mes.weekday())


    detalles = []
    cal_mes = []
    week = []
    week_headers = []


    i = 0
    dia = primer_dia_calendario
    while dia <= ultimo_dia_calendario:
        if i < 7:
            week_headers.append(dia)
        cal_day = {}
        cal_day['day'] = dia
        cal_day['event'] = False
        for evento in eventos_owner_lista:
            if dia == evento.fecha.date():
                cal_day['event'] = True
                if getDetalle:
                    if dia == nueva_fecha:
                        detalles.append(evento)

        if dia.month == month:
            cal_day['in_month'] = True
        else:
            cal_day['in_month'] = False
        week.append(cal_day)
        if dia.weekday() == 6:
            cal_mes.append(week)
            week = []
        i += 1
        dia += timedelta(1)
    mesCal = getMesEspañol(fecha_pedida)
    añoCal = fecha_pedida.strftime("%Y")

    return render(request, 'cal_mes.html',
                  {'mesCal': mesCal, 'anoCal': añoCal, 'calendar': cal_mes, 'headers': week_headers,
                  'getDetalle': getDetalle, 'detalles': detalles, "getMes": getMes, 'masMes': fecha})

def getMesEspañol(fecha):
    numeroMes = fecha.month

    if numeroMes ==1:
        res = 'Enero'
    elif numeroMes ==2:
        res = 'Febrero'
    elif numeroMes ==3:
        res = 'Marzo'
    elif numeroMes ==4:
        res = 'Abril'
    elif numeroMes ==5:
        res = 'Mayo'
    elif numeroMes ==6:
        res = 'Junio'
    elif numeroMes ==7:
        res = 'Julio'
    elif numeroMes ==8:
        res = 'Agosto'
    elif numeroMes ==9:
        res = 'Septiembre'
    elif numeroMes ==10:
        res = 'Octubre'
    elif numeroMes ==11:
        res = 'Noviembre'
    else:
        res = 'Diciembre'


    return res



def getValores(dic_solicitud):
    try:
        fechaDetalle =  dic_solicitud["detalle"]

    except:
        fechaDetalle = ""

    try:
        fecha = dic_solicitud["fecha"]
    except:
        fecha = ""

    return fechaDetalle, fecha

