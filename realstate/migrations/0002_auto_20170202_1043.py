# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 16:43
from __future__ import unicode_literals

from django.db import migrations
import fontawesome.fields


class Migration(migrations.Migration):

    dependencies = [
        ('realstate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_contacto',
            name='icono',
            field=fontawesome.fields.IconField(blank=True, max_length=60),
        ),
    ]
