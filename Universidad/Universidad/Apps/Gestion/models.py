# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Mama(models.Model):
    nombre = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=40)
    email = models.EmailField()
    fechaNacimiento = models.DateField()
    direccion =models.CharField(max_length=55)
    fechaUltMens = models.DateField()

    def __str__(self):
        return self.nombre + " " + self.apellidos


class Calendario (models.Model):
    mama = models.OneToOneField(Mama, null = False, default='DEFAULT VALUE')

class Fecha(models.Model):
    titulo = models.CharField(max_length=25)
    momentoInicio = models.DateTimeField ()
    momentoFin = models.DateTimeField ()
    calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE, null=False, blank=False, default='DEFAULT VALUE')

    def __str__(self):
        return self.titulo

class Diario(models.Model):
    mama = models.OneToOneField(Mama, null = False, default='DEFAULT VALUE')

class Medida(models.Model):
    fecha = models.DateField()
    dBiparieta = models.IntegerField()
    cAbdominal = models.IntegerField()
    lFemur = models.IntegerField()
    diario = models.ForeignKey(Diario, on_delete=models.CASCADE, null=False, blank=False, default='DEFAULT VALUE')


class Fotografia(models.Model):
    enlace = models.CharField(max_length=1000)
    despription = models.CharField(max_length=1000, null=True, blank = True)
    diario = models.ForeignKey(Diario, on_delete=models.CASCADE, null=False, blank=False, default='DEFAULT VALUE')

class Patada(models.Model):
    momento = models.DateTimeField ()
    despription = models.CharField(max_length=1000, null=True, blank = True)
    diario = models.ForeignKey(Diario, on_delete=models.CASCADE, null=False, blank=False, default='DEFAULT VALUE')

class Tension(models.Model):
    momento = models.DateTimeField ()
    tSistolica = models.DecimalField(max_digits=4, decimal_places=2)
    tDiastolica = models.DecimalField(max_digits=4, decimal_places=2)
    diario = models.ForeignKey(Diario, on_delete=models.CASCADE, null=False, blank=False, default='DEFAULT VALUE')

class Medicacion(models.Model):
    medicamento = models.CharField(max_length=50)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    frecuencia = models.IntegerField()
    diario = models.ForeignKey(Diario, on_delete=models.CASCADE, null=False, blank=False, default='DEFAULT VALUE')

class Peso(models.Model):
    tipo_choice = (
        ('Madre', 'Madre'),
        ('Bebe', 'Bebe')
    )

    fecha = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    tipo = models.CharField(max_length=100, choices=tipo_choice)
    diario = models.ForeignKey(Diario, on_delete=models.CASCADE, null=False, blank=False, default='DEFAULT VALUE')

class Contraccion(models.Model):
    momento = models.DateTimeField ()
    despription = models.CharField(max_length=1000, null=True)
    diario = models.ForeignKey(Diario, on_delete=models.CASCADE, null=False, blank=False, default='DEFAULT VALUE')






