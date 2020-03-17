# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from django.contrib import admin
from CuarentaSemanas.Apps.Gestion.models import User, Diario, Calendario, \
    Fecha, Medida, Fotografia, Patada, Tension, Medicacion, Peso, Contraccion
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth import get_user_model

User=get_user_model()

# Register your models here.
#admin.site.register(User)
#admin.site.register(User)
admin.site.register(Diario)
admin.site.register(Calendario)
admin.site.register(Fecha)
admin.site.register(Medida)
admin.site.register(Fotografia)
admin.site.register(Peso)
admin.site.register(Patada)
admin.site.register(Tension)
admin.site.register(Medicacion)
admin.site.register(Contraccion)


admin.site.unregister(Group)