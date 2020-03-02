# -*- coding: utf-8 -*-
from django.http import HttpResponse

from django.shortcuts import render, redirect
from .forms import MamaCreateForm, EditarPerfilForm
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm



# Create your views here.


def inicio(request):
    return render(request, 'inicio.html')


def inicioSesion(request):
    return render(request, 'inicioSesion.html')

def miPerfil(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'miPerfil.html', {"user": user})

def borrarUsuario(request, id_user):
    User = get_user_model()
    user = User.objects.get(id=id_user)
    if request.method == "POST":
        user.delete()
        return render(request, 'inicio.html')
    context = {
        "User": user
    }
    return render(request, "borrarUsuario.html", context)

def editarPerfil(request,id_user):
    User = get_user_model()
    user=User.objects.get(id=id_user)
    if request.method == 'GET':
        form=EditarPerfilForm(instance=user)
    else:
        form=EditarPerfilForm(request.POST,instance=user)
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
