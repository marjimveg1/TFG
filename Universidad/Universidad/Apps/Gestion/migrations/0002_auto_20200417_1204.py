# Generated by Django 3.0.4 on 2020-04-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patada',
            name='numero',
            field=models.IntegerField(),
        ),
    ]