# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from django.contrib import admin
from Universidad.Apps.Gestion.models import Alumno
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth import get_user_model

User=get_user_model()

# Register your models here.
#admin.site.register(User)
admin.site.register(Alumno)

class UserAdmin(BaseUserAdmin):



    list_display = ('Apellido', 'Nombre')
    fieldsets = (
        (None, {'fields': ('Apellido', 'Nombre')})
    )


admin.site.unregister(Group)