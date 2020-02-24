# -*- coding: utf-8 -*-
from django.http import HttpResponse


from django.shortcuts import render, redirect
from .forms import MamaCreateForm


# Create your views here.


def inicio(request):
    return render(request, 'inicio.html')


def inicioSesion(request):
    return render(request, 'inicioSesion.html')


#REGISTRO DE USUARIOS
def registro(request):
    if request.method == 'POST':
        form = MamaCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/inicio/')
        else:
            return render(request, 'base.html', {'form': form})
    else:
        form = MamaCreateForm()
    return render(request, 'registro.html', {'form': form})