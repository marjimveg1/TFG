# -*- coding: utf-8 -*-
from builtins import print

from django.http import HttpResponse

from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from datetime import date, timedelta, datetime
from .models import *
from django.shortcuts import render
from django.core.paginator import Paginator
from django.conf import settings
from decimal import  Decimal

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


# DIARIO
def diario(request):
    return render(request, 'diarioSeguimiento/diarioSeguimiento.html')

#TENSION


def inicioTension(request):
    lista_tension = {}
    page = ""
    if request.user.is_authenticated:
        user = request.user
        diario_owner = Diario.objects.filter(user=user)[0]
        lista_tension = Tension.objects.filter(diario=diario_owner).order_by('momento')

        paginator = Paginator(lista_tension, 10)
        page = request.GET.get('pagina')
        lista_tension = paginator.get_page(page)

    return render(request, 'diarioSeguimiento/inicioTension.html', {"lista_tension": lista_tension, 'page':page, 'MEDIA_URL': settings.MEDIA_URL})

def anadirTension(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = CrearTensionForm(request.POST)
            if form.is_valid():
                diario = Diario.objects.filter(user=user)[0]
                obj = form.save(commit=False)
                obj.diario = diario
                form.save()
                return redirect('/inicioTension/')
        else:
            form = CrearTensionForm()

    return render(request, 'diarioSeguimiento/anadirTension.html', {'form': form})

def borrarTension(request, idTension):
    tension = Tension.objects.get(id=idTension)
    user = request.user
    diario = Diario.objects.filter(user=user)[0]
    lista_tension = Tension.objects.filter(diario=diario)

    if tension in lista_tension:
        tension.delete()
    return redirect('/inicioTension/')


def inicioPesoMama(request):
    lista_peso = {}
    page = ""
    if request.user.is_authenticated:
        user = request.user
        diario_owner = Diario.objects.filter(user=user)[0]
        lista_peso = Peso.objects.filter(diario=diario_owner, tipo="Madre").order_by('fecha')

        paginator = Paginator(lista_peso, 10)
        page = request.GET.get('pagina')
        lista_peso = paginator.get_page(page)

    return render(request, 'diarioSeguimiento/inicioPeso.html', {"isMama":True, "lista_peso": lista_peso, 'page':page, 'MEDIA_URL': settings.MEDIA_URL})

def anadirPesoMama(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = CrearPesoForm(request.POST)
            if form.is_valid():
                diario = Diario.objects.filter(user=user)[0]
                obj = form.save(commit=False)
                obj.diario = diario
                obj.tipo = "Madre"
                form.save()
                return redirect('/inicioPesoMama/')
        else:
            form = CrearPesoForm()

    return render(request, 'diarioSeguimiento/anadirPesoMama.html', {'form': form})

def borrarPeso(request, idPeso):
    peso = Peso.objects.get(id=idPeso)
    user = request.user
    diario = Diario.objects.filter(user=user)[0]
    lista_peso = Peso.objects.filter(diario=diario)

    if peso in lista_peso:
        peso.delete()
    return redirect('/miDiario/')


def inicioPesoBebe(request):
    lista_peso = {}
    page = ""
    if request.user.is_authenticated:
        user = request.user
        diario_owner = Diario.objects.filter(user=user)[0]
        lista_peso = Peso.objects.filter(diario=diario_owner, tipo="Bebe").order_by('fecha')

        paginator = Paginator(lista_peso, 10)
        page = request.GET.get('pagina')
        lista_peso = paginator.get_page(page)

    return render(request, 'diarioSeguimiento/inicioPeso.html', {"isMama":False, "lista_peso": lista_peso, 'page':page, 'MEDIA_URL': settings.MEDIA_URL})

def anadirPesoBebe(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = CrearPesoForm(request.POST)
            if form.is_valid():
                diario = Diario.objects.filter(user=user)[0]
                obj = form.save(commit=False)
                obj.diario = diario
                obj.tipo = "Bebe"
                form.save()
                return redirect('/inicioPesoBebe/')
        else:
            form = CrearPesoForm()

    return render(request, 'diarioSeguimiento/anadirPesoBebe.html', {'form': form})

def inicioPatada(request):
    # if request.user.is_authenticated:
    #     user = request.user
    #     diario = Diario.objects.filter(user=user)[0]
    #     if request.method == 'POST':
    #         fecha = request.POST['form_fecha']
    #         duracion = request.POST['form_duracion']
    #         intervalo = request.POST['form_intervalo']
    #         crearContracciones(fecha,duracion,intervalo,diario)
    #         return redirect('/inicioContraccion/')

    return render(request, 'diarioSeguimiento/inicioPatada.html')


def inicioMedicacion(request):
    lista_medicacion = {}
    page = ""
    if request.user.is_authenticated:
        user = request.user
        diario_owner = Diario.objects.filter(user=user)[0]
        lista_medicacion = Medicacion.objects.filter(diario=diario_owner).order_by('fechaInicio')

        paginator = Paginator(lista_medicacion, 10)
        page = request.GET.get('pagina')
        lista_medicacion = paginator.get_page(page)

    return render(request, 'diarioSeguimiento/inicioMedicacion.html', {"lista_medicacion": lista_medicacion, 'page':page, 'MEDIA_URL': settings.MEDIA_URL})

def anadirMedicacion(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = CrearMedicacionForm(request.POST)
            if form.is_valid():
                diario = Diario.objects.filter(user=user)[0]
                obj = form.save(commit=False)
                obj.diario = diario
                form.save()
                return redirect('/miDiario/')
        else:
            form = CrearMedicacionForm()

    return render(request, 'diarioSeguimiento/anadirMedicacion.html', {'form': form})

def borrarMedicacion(request, idMedicacion):
    medicacion = Medicacion.objects.get(id=idMedicacion)
    user = request.user
    diario = Diario.objects.filter(user=user)[0]
    lista_medicacion = Medicacion.objects.filter(diario=diario)

    if medicacion in lista_medicacion:
        medicacion.delete()
    return redirect('/inicioMedicacion/')


def inicioContraccion(request):
    if request.user.is_authenticated:
        user = request.user
        diario = Diario.objects.filter(user=user)[0]
        if request.method == 'POST':
            fecha = request.POST['form_fecha']
            duracion = request.POST['form_duracion']
            intervalo = request.POST['form_intervalo']
            crearContracciones(fecha,duracion,intervalo,diario)
            return redirect('/inicioContraccion/')

    return render(request, 'diarioSeguimiento/inicioContraccion.html')

def crearContracciones(fecha,duracion,intervalo,diario):
    intervalo = intervalo + "00.00;"
    lista_fecha = fecha.split(";")
    lista_duracion = duracion.split(";")
    lista_intervalo = intervalo.split(";")



    for i in range(0,len(lista_fecha)-1):
        fecha = lista_fecha[i]
        duracion = lista_duracion[i]
        intervalo = lista_intervalo[i]
        contraccion = Contraccion(diario=diario, duración=Decimal(duracion.strip(' "')), intervalo=Decimal(intervalo.strip(' "')), momento=fecha)
        contraccion.save()

    return lista_fecha,lista_intervalo,lista_duracion;



def inicioMedida(request):
    lista_medida = {}
    page = ""
    if request.user.is_authenticated:
        user = request.user
        diario_owner = Diario.objects.filter(user=user)[0]
        lista_medida = Medida.objects.filter(diario=diario_owner).order_by('fecha')

        paginator = Paginator(lista_medida, 10)
        page = request.GET.get('pagina')
        lista_medida = paginator.get_page(page)

    return render(request, 'diarioSeguimiento/inicioMedida.html', {"lista_medida": lista_medida, 'page':page, 'MEDIA_URL': settings.MEDIA_URL})

def anadirMedida(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = CrearMedidaForm(request.POST)
            if form.is_valid():
                diario = Diario.objects.filter(user=user)[0]
                obj = form.save(commit=False)
                obj.diario = diario
                form.save()
                return redirect('/miDiario/')
        else:
            form = CrearMedidaForm()

    return render(request, 'diarioSeguimiento/anadirMedida.html', {'form': form})

def borrarMedida(request, idMedida):
    medida = Medida.objects.get(id=idMedida)
    user = request.user
    diario = Diario.objects.filter(user=user)[0]
    lista_medida = Medida.objects.filter(diario=diario)

    if medida in lista_medida:
        medida.delete()
    return redirect('/inicioMedida/')


# CALENDARIO
def buscarFecha(request):
    return render(request, 'agenda/buscarFecha.html')


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

    return render(request, 'agenda/anadirFechaCalendario.html', {'form': form})





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

    return render(request, 'agenda/cal_mes.html',
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

