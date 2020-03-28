# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from Universidad.Apps.Gestion.models import *


User = get_user_model()


# REGISTRO DE UN USUARIO (MAMÁ)
class MamaCreateForm(UserCreationForm):
    formato = ("Format: dd/mm/YYYY"),


    nombre = forms.CharField(label=('Nombre'), required=True)
    apellidos = forms.CharField(label=('Apellidos'), required=True)
    email = forms.CharField(label=('Email'), required=True)
    fechaNacimiento = forms.DateField(label=('Fecha de nacimiento'), input_formats=['%d/%m/%Y'], help_text=formato, required=False)
    direccion = forms.CharField(label=('Dirección'), required=False)
    fechaUltMens = forms.DateField(label=('Última menstruación'), input_formats=['%d/%m/%Y'], help_text=formato, required=True)
    nickName = forms.CharField(label=('Nombre de usuario'), max_length=50, required=True)

    class Meta:
        model = User
        fields = ( "nombre", "apellidos",  "email", "fechaNacimiento","direccion","fechaUltMens","nickName","password1", "password2")

    def save(self):
        user = super(MamaCreateForm, self).save(commit=False)
        user.nombre = self.cleaned_data["nombre"]
        user.apellidos = self.cleaned_data["apellidos"]
        user.nickName = self.cleaned_data["nickName"]
        user.fechaNacimiento = self.cleaned_data["fechaNacimiento"]
        user.fechaUltMens = self.cleaned_data["fechaUltMens"]
        user.direccion = self.cleaned_data["direccion"]
        user.email = self.cleaned_data["email"]
        user.save()

        calendario = Calendario()
        calendario.nombre = "calendario"
        calendario.user = user
        calendario.save()

        return user

    def clean(self, *args, **kwargs):
        cleaned_data = super(MamaCreateForm, self).clean(*args, **kwargs)
        nickName = cleaned_data.get('nickName', None)
        # Recorremos todos los usuarios para ver si ya existe
        if nickName is not None:
            users = User.objects.all()
            for u in users:
                if nickName == u.nickName:
                    self.add_error('nickName', ('Nick Name ya existe'))
                    break

        year_birth = cleaned_data.get('fechaNacimiento', None)
        # Comprobamos que la fecha de nacimiento sea en pasado
        if year_birth is not None:
            now = timezone.now()
            if year_birth > now:
                self.add_error('fechaNacimiento', ('No puede ser futuro'))

        fecha_mens = cleaned_data.get('fechaUltMens', None)
        if fecha_mens is not None:
            now = timezone.now()
            if fecha_mens > now:
                self.add_error('fechaUltMens', ('No puede ser futuro'))


class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('nickName','nombre','apellidos','direccion','fechaNacimiento', 'fechaUltMens')

    def clean_password(self):
        return self.initial["password"]



class FechaCalendarioForm(forms.ModelForm):

    class Meta:
        model = Evento
        exclude = {'calendario',}
        fields = ['titulo','fecha','descripcion',]

        labels = {
            'titulo': 'Titulo',
            'fecha': 'Fecha',
            'descripcion': 'Descripcion',

        }




class BuscarFechaForm(forms.ModelForm):
    class Meta:
        fields = ['mes','año',]

        labels = {
            'mes': 'Mes',
            'año': 'Año',

        }

        widgets = {
            'mes': forms.TextInput(attrs={'class':'form-control'}),
            'año': forms.TextInput(attrs={'class':'form-control'}),
        }
