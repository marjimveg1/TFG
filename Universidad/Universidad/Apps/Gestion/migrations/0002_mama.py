# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-09 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellidos', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('fechaNacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=55)),
                ('fechaUltMens', models.DateField()),
            ],
        ),
    ]
