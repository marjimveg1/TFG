# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from Universidad.Apps.Gestion.models import *


User = get_user_model()


# REGISTRO DE UN USUARIO (MAMÁ)
class MamaCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ( "nombre", "apellidos",  "email", "direccion","fechaNacimiento","fechaUltMens","nickName","password1", "password2")

        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'email': 'Correo electrónico',
            'dirección': 'Dirección',
            'fechaNacimiento': 'Fecha de nacimiento',
            'fechaUltMens': 'Fecha última menstruación',
            'nickName': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirme contraseña',

        }

    widgets = {
        'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        'fechaNacimiento': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),
        'fechaUltMens': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),
        'nickName': forms.TextInput(attrs={'class': 'form-control'}),
        'password1': forms.TextInput(attrs={'class': 'form-control'}),
        'password2': forms.TextInput(attrs={'class': 'form-control'}),
    }


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

        diario = Diario()
        diario.nombre = "diario"
        diario.user = user
        diario.save()

        evento_fechaUltMenst = Evento()
        evento_fechaUltMenst.titulo = "Última menstruación"
        evento_fechaUltMenst.fecha = user.fechaUltMens
        evento_fechaUltMenst.calendario = calendario
        evento_fechaUltMenst.save()


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
            now = timezone.now().date()
            if year_birth > now:
                self.add_error('fechaNacimiento', ('No puede ser futuro'))

        fecha_mens = cleaned_data.get('fechaUltMens', None)
        if fecha_mens is not None:
            now = timezone.now().date()
            if fecha_mens > now:
                self.add_error('fechaUltMens', ('No puede ser futuro'))


class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('nombre','apellidos','direccion','fechaNacimiento', 'fechaUltMens')

        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'dirección': 'Dirección',
            'fechaNacimiento': 'Fecha de nacimiento',
            'fechaUltMens': 'Fecha última menstruación',

        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'dirección': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaNacimiento': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),
            'fechaUltMens': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'})
        }

    def clean(self, *args, **kwargs):
        cleaned_data = super(EditarPerfilForm, self).clean(*args, **kwargs)

        year_birth = cleaned_data.get('fechaNacimiento', None)
        # Comprobamos que la fecha de nacimiento sea en pasado
        if year_birth is not None:
            now = timezone.now().date()
            if year_birth > now:
                self.add_error('fechaNacimiento', ('No puede ser futuro'))

        fecha_mens = cleaned_data.get('fechaUltMens', None)
        if fecha_mens is not None:
            now = timezone.now().date()
            if fecha_mens > now:
                self.add_error('fechaUltMens', ('No puede ser futuro'))


class CrearTensionForm(forms.ModelForm):

    class Meta:
        model = Tension
        exclude = {'diario',}
        fields = ['momento','tSistolica','tDiastolica',]

        labels = {
            'momento': 'Fecha',
            'tSistolica': 'Tensión sistólica',
            'tDiastolica': 'Tensión diastólica',

        }
        widgets = {
            'momento': forms.DateTimeInput(attrs={'placeholder': 'dd/mm/aaaa hh:mm'}),
            'tSistolica': forms.NumberInput(),
            'tDiastolica' : forms.NumberInput(),
        }

class CrearPesoForm(forms.ModelForm):

    class Meta:
        model = Peso
        exclude = {'diario','tipo'}
        fields = ['fecha','peso',]

        labels = {
            'fecha': 'Fecha',
            'peso': 'Peso',

        }
        widgets = {
            'fecha': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),
            'peso': forms.NumberInput(),
        }

class CrearPatadaForm(forms.ModelForm):

    class Meta:
        model = Patada
        exclude = {'diario','momento'}
        fields = ['despripcion',]

        labels = {
            'despripcion': 'Descripción',

        }
        widgets = {
            'despripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CrearMedicacionForm(forms.ModelForm):

    class Meta:
        model = Medicacion
        exclude = {'diario',}
        fields = ['medicamento','fechaInicio','fechaFin', 'frecuencia']

        labels = {
            'medicamento': 'Medicamento',
            'fechaInicio': 'Fecha de inicio del tratamiento',
            'fechaFin': 'Fecha de fin del tratamiento',
            'frecuencia': 'Frecuencia de tomas',

        }
        widgets = {
            'medicamento': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaInicio': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),
            'fechaFin': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),
            'frecuencia': forms.NumberInput(),
        }

class CrearContraccionForm(forms.ModelForm):

    class Meta:
        model = Contraccion
        exclude = {'diario','momento'}
        fields = ['despripcion',]

        labels = {
            'despripcion': 'Descripción',

        }
        widgets = {
            'despripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }




class FechaCalendarioForm(forms.ModelForm):

    class Meta:
        model = Evento
        exclude = {'calendario',}
        fields = ['titulo','fecha','descripcion',]

        labels = {
            'titulo': 'Título',
            'fecha': 'Fecha',
            'descripcion': 'Descripción',

        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateTimeInput(attrs={'placeholder': 'dd/mm/aaaa hh:mm'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'})
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
