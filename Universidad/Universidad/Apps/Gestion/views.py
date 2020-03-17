# -*- coding: utf-8 -*-
from builtins import print

from django.http import HttpResponse

from django.shortcuts import render, redirect
from .forms import MamaCreateForm, EditarPerfilForm, FechaCalendarioForm
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import DayArchiveView, YearArchiveView, TodayArchiveView
from django.urls import reverse_lazy
import calendar

from .models import *
from django import template
from datetime import date, timedelta
from .models import Fecha
from .utils import Calendar


from datetime import datetime, date

from django.shortcuts import render
from django.utils.safestring import mark_safe
from .util import Calendar
from django.views.generic.list import ListView

# Create your views here.


def inicio(request):
    return render(request, 'inicio.html')


def inicioSesion(request):
    return render(request, 'inicioSesion.html')


def miPerfil(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'miPerfil.html', {"user": user})


def borrarUsuario(request):
    User = get_user_model()
    user = request.user
    if request.method == "POST":
        user.delete()
        return render(request, 'inicio.html')
    context = {
        "User": user
    }
    return render(request, "borrarUsuario.html", context)


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
    if request.method == 'POST':
        form = MamaCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/inicio/')
    else:
        form = MamaCreateForm()
    return render(request, 'registro.html', {'form': form})


# CALENDARIO
def miCalendario(request):
    if request.user.is_authenticated:
        user = request.user
        fechas = Fecha.objects.filter(calendario=(Calendario.objects.filter(user=user)[0]))

        return render(request, 'miCalendario.html', {"fechas": fechas})


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
                return redirect('/miCalendario/')
        else:
            form = FechaCalendarioForm()

    return render(request, 'anadirFechaCalendario.html', {'form': form})


def miCalendario1(ListView):
    model = Fecha
    template_name = "calendario.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def EntradasDia(request):
    user = request.user
    calendario_owner = Calendario.objects.filter(user=user)[0]
    year = 2012
    month = 1
    event_list = Fecha.objects.filter(calendario = calendario_owner)
   # event_list = Fecha.objects.filter(momentoInicio__year=year, momentoFin__month=month, calendario=calendario_owner )
    first_day_of_month = date(year, month, 1)
    if (month == 12):
        year += 1
        month = 1
    else:
        month += 1
    last_day_of_month = date(year, month, 1) - timedelta(1)
    first_day_of_calendar = first_day_of_month - timedelta(first_day_of_month.weekday())
    last_day_of_calendar = last_day_of_month + timedelta(7 - last_day_of_month.weekday())


    cal_mes = []
    week = []
    week_headers = []

    i = 0
    day = first_day_of_calendar
    while day <= last_day_of_calendar:
        if i < 7:
            week_headers.append(day)
        cal_day = {}
        cal_day['day'] = day
        cal_day['event'] = False
        for event in event_list:
            if day >= event.momentoInicio.date() and day <= event.momentoInicio.date():
                cal_day['event'] = True
        if day.month == month:
            cal_day['in_month'] = True
        else:
            cal_day['in_month'] = False
        week.append(cal_day)
        if day.weekday() == 6:
            cal_mes.append(week)
            week = []
        i += 1
        day += timedelta(1)
    print(week_headers)

    return render(request,'cal_mes.html', {'calendar': cal_mes, 'headers': week_headers})


class CalendarView(ListView):
    model = Fecha
    template_name = 'calendar.html'
    success_url = reverse_lazy('calendar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        prev_month = int(d.strftime('%m')) -1
        next_month = int(d.strftime('%m')) + 1
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month
        context['next_month'] = next_month
        return context
