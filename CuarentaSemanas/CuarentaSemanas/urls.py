from django.conf.urls import url
from CuarentaSemanas.Apps.Gestion.views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, re_path
from django.contrib.auth import views as auth_views
from CuarentaSemanas.Apps.Gestion.views import *


urlpatterns = [
    url('admin/', admin.site.urls),
    url('inicio/', inicio),
    url('registro/', registro),
    url('miPerfil/', miPerfil),

    url(r'editarPerfil/(?P<id_user>\d+)', editarPerfil,name='editarPerfil'),
    url(r'borrarUsuario/(?P<id_user>\d+)', borrarUsuario, name='borrarUsuario'),
    url(r'cambiarContra/$', cambiar_contra, name='cambiarContra'),

    url('miCalendario/',miCalendario, name='miCalendario'),
    url('anadirFecha/',crearFechaCalendario, name='anadirFecha'),
    url('miCalendario1/',miCalendario1, name='anadirFecha'),

    url('inicioSesion/', auth_views.LoginView.as_view(), name='inicioSesion'),
    url('cerrarSesion/', auth_views.LogoutView.as_view(), name='logout'),
]


