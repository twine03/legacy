# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 17:53
from __future__ import unicode_literals

from django.db import migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('realstate', '0003_auto_20170203_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='position',
            field=geoposition.fields.GeopositionField(blank=True, max_length=42, null=True),
        ),
    ]
