# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from django.contrib import admin
from Universidad.Apps.Gestion.models import Mama, Calendario, Fecha, Diario,Medicacion,Medida,Fotografia,Tension,Patada,Peso,Contraccion
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth import get_user_model

User=get_user_model()

# Register your models here.
#admin.site.register(User)
admin.site.register(Mama)
admin.site.register(Calendario)
admin.site.register(Diario)
admin.site.register(Fecha)
admin.site.register(Medida)
admin.site.register(Tension)
admin.site.register(Medicacion)
admin.site.register(Contraccion)
admin.site.register(Fotografia)
admin.site.register(Patada)
admin.site.register(Peso)


class UserAdmin(BaseUserAdmin):



    list_display = ('Apellido', 'Nombre')
    fieldsets = (
        (None, {'fields': ('Apellido', 'Nombre')})
    )


admin.site.unregister(Group)