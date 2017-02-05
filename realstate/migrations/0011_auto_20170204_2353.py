# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 05:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realstate', '0010_auto_20170204_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propiedad',
            name='galerias',
        ),
        migrations.AddField(
            model_name='propiedad',
            name='fotos',
            field=models.ManyToManyField(blank=True, null=True, to='realstate.Foto'),
        ),
        migrations.AlterField(
            model_name='foto',
            name='galeria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='realstate.Galeria'),
        ),
    ]