# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-20 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Contraccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('momento', models.DateTimeField()),
                ('despription', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Fecha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=25)),
                ('momentoInicio', models.DateTimeField()),
                ('momentoFin', models.DateTimeField()),
                ('calendario', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='Gestion.Calendario')),
            ],
        ),
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enlace', models.CharField(max_length=1000)),
                ('despription', models.CharField(blank=True, max_length=1000, null=True)),
                ('diario', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='Gestion.Diario')),
            ],
        ),
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
        migrations.CreateModel(
            name='Medicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicamento', models.CharField(max_length=50)),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('frecuencia', models.IntegerField()),
                ('diario', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='Gestion.Diario')),
            ],
        ),
        migrations.CreateModel(
            name='Medida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('dBiparieta', models.IntegerField()),
                ('cAbdominal', models.IntegerField()),
                ('lFemur', models.IntegerField()),
                ('diario', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='Gestion.Diario')),
            ],
        ),
        migrations.CreateModel(
            name='Patada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('momento', models.DateTimeField()),
                ('despription', models.CharField(blank=True, max_length=1000, null=True)),
                ('diario', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='Gestion.Diario')),
            ],
        ),
        migrations.CreateModel(
            name='Peso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tipo', models.CharField(choices=[('Madre', 'Madre'), ('Bebe', 'Bebe')], max_length=100)),
                ('diario', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='Gestion.Diario')),
            ],
        ),
        migrations.CreateModel(
            name='Tension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('momento', models.DateTimeField()),
                ('tSistolica', models.DecimalField(decimal_places=2, max_digits=4)),
                ('tDiastolica', models.DecimalField(decimal_places=2, max_digits=4)),
                ('diario', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='Gestion.Diario')),
            ],
        ),
        migrations.AddField(
            model_name='diario',
            name='mama',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='Gestion.Mama'),
        ),
        migrations.AddField(
            model_name='contraccion',
            name='diario',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='Gestion.Diario'),
        ),
        migrations.AddField(
            model_name='calendario',
            name='mama',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='Gestion.Mama'),
        ),
    ]
