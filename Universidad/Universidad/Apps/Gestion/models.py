# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Alumno(models.Model):
    Apellido = models.CharField(max_length=35)
    Nombre = models.CharField(max_length=35)

    def NombreCompleto(self):
        cadena = "{0} {1}"

        return cadena.format(self.Apellido, self.Nombre)




    def __str__(self):
        return self.NombreCompleto()
# Create your models here.
