# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager


#class Mama(models.Model):
class User(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=60, null=True)
    email = models.EmailField()
    fechaNacimiento = models.DateField()
    direccion = models.CharField(max_length=55)
    fechaUltMens = models.DateField()
    nickName = models.CharField(('Nick Name'), unique=True, max_length=50)

    objects = UserManager()
    USERNAME_FIELD = 'nickName'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nickName

class Calendario (models.Model):
    nombre = models.CharField(max_length=25,default='SOME STRING')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

class Fecha(models.Model):
    titulo = models.CharField(max_length=25)
    momentoInicio = models.DateTimeField ()
    momentoFin = models.DateTimeField ()
    calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE, null=False, blank=False)

class Diario(models.Model):
    nombre = models.CharField(max_length=25,default='SOME STRING')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.titulo

class Medida(models.Model):
    fecha = models.DateField()
    dBiparieta = models.IntegerField()
    cAbdominal = models.IntegerField()
    lFemur = models.IntegerField()
    diario = models.ForeignKey(Diario, on_delete=models.CASCADE, null=False, blank=False)


class Fotografia(models.Model):
    enlace = models.CharField(max_length=1000)
    despription = models.CharField(max_length=1000, null=True, blank = True)
    diario = models.ForeignKey(Diario, on_delete=models.CASCADE, null=False, blank=False)


class Patada(models.Model):
    momento = models.DateTimeField ()
    despription = models.CharField(max_length=1000, null=True, blank = True)
    diario = models.ForeignKey(Diario, on_delete=models.CASCADE, null=False, blank=False)

class Tension(models.Model):
    momento = models.DateTimeField ()
    tSistolica = models.DecimalField(max_digits=4, decimal_places=2)
    tDiastolica = models.DecimalField(max_digits=4, decimal_places=2)
    diario = models.ForeignKey(Diario, on_delete=models.CASCADE, null=False, blank=False)


class Medicacion(models.Model):
    medicamento = models.CharField(max_length=50)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    frecuencia = models.IntegerField()
    diario = models.ForeignKey(Diario, on_delete=models.CASCADE, null=False, blank=False)

class Peso(models.Model):
    tipo_choice = (
        ('Madre', 'Madre'),
        ('Bebe', 'Bebe')
    )

    fecha = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    tipo = models.CharField(max_length=100, choices=tipo_choice)
    diario = models.ForeignKey(Diario, on_delete=models.CASCADE, null=False, blank=False)

class Contraccion(models.Model):
    momento = models.DateTimeField ()
    despription = models.CharField(max_length=1000, null=True)
    diario = models.ForeignKey(Diario, on_delete=models.CASCADE, null=False, blank=False)



