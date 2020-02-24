# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

User = get_user_model()


# REGISTRO DE UN USUARIO (MAMÁ)

class MamaCreateForm(UserCreationForm):
    formato = ("Format: dd/mm/YYYY"),

    nickName = forms.CharField(label=('Nick Name'), max_length=50, required=True)
    nombre = forms.CharField(label=('Nombre'), required=True)
    apellidos = forms.CharField(label=('Apellidos'), required=True)
    email = forms.CharField(label=('email'), required=True)
    fechaNacimiento = forms.DateTimeField(label=('Fecha de nacimiento'), input_formats=['%d/%m/%Y'], help_text=formato, required=True)
    fechaUltMens = forms.DateTimeField(label=('Ultima menstruacion'), input_formats=['%d/%m/%Y'], help_text=formato, required=True)
    direccion = forms.CharField(label=('Direccion'), required=False)

    class Meta:
        model = User
        fields = ("nickName","nombre", "apellidos", "email", "fechaNacimiento", "fechaUltMens","direccion", "password1", "password2")

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
                self.add_error('year_birth', ('Np ìede ser futuro'))
