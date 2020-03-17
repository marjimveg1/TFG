"""Universidad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from Universidad.Apps.Gestion.views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, re_path
from django.contrib.auth import views as auth_views
from Universidad.Apps.Gestion.views import *


urlpatterns = [
    url('admin/', admin.site.urls),
    url('inicio/', inicio),
    url('registro/', registro),
    url('miPerfil/', miPerfil),

    url('editarPerfil/', editarPerfil,name='editarPerfil'),
    url('borrarUsuario/', borrarUsuario, name='borrarUsuario'),
    url('cambiarContra/', cambiar_contra, name='cambiarContra'),

    url('miCalendario/',miCalendario, name='miCalendario'),
    url('anadirFecha/',crearFechaCalendario, name='anadirFecha'),
    url('miCalendario1/',miCalendario1, name='anadirFecha'),

    url('inicioSesion/', auth_views.LoginView.as_view(), name='inicioSesion'),
    url('cerrarSesion/', auth_views.LogoutView.as_view(), name='logout'),
url('blog/',
    EntradasDia, name='entradas'),
url(r'^calendar/$', CalendarView.as_view(), name='calendar'),
]