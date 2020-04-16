# Generated by Django 3.0.4 on 2020-04-16 16:26

import Universidad.Apps.Gestion.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='SOME STRING', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Diario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='SOME STRING', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=60, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('fechaNacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=55)),
                ('fechaUltMens', models.DateField()),
                ('nickName', models.CharField(max_length=50, unique=True, verbose_name='Nick Name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is staf')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', Universidad.Apps.Gestion.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Tension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('momento', models.DateTimeField()),
                ('tSistolica', models.DecimalField(decimal_places=2, max_digits=4)),
                ('tDiastolica', models.DecimalField(decimal_places=2, max_digits=4)),
                ('diario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.Diario')),
            ],
        ),
        migrations.CreateModel(
            name='Peso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tipo', models.CharField(choices=[('Madre', 'Madre'), ('Bebe', 'Bebe')], max_length=100)),
                ('diario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.Diario')),
            ],
        ),
        migrations.CreateModel(
            name='Patada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('momento', models.DateTimeField()),
                ('despripcion', models.CharField(blank=True, max_length=1000, null=True)),
                ('diario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.Diario')),
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
                ('diario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.Diario')),
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
                ('diario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.Diario')),
            ],
        ),
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enlace', models.CharField(max_length=1000)),
                ('despripcion', models.CharField(blank=True, max_length=1000, null=True)),
                ('diario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.Diario')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=350)),
                ('categoria', models.CharField(choices=[('Cita médico', 'Cita médico'), ('Recordatorio', 'Recordatorio')], max_length=100)),
                ('fecha', models.DateTimeField()),
                ('calendario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.Calendario')),
            ],
        ),
        migrations.AddField(
            model_name='diario',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Contraccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('momento', models.DateTimeField()),
                ('duración', models.IntegerField()),
                ('intervalo', models.IntegerField()),
                ('diario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.Diario')),
            ],
        ),
        migrations.AddField(
            model_name='calendario',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
