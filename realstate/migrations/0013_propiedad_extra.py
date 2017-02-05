# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realstate', '0012_auto_20170205_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propiedad_Extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('valor', models.CharField(max_length=300)),
                ('propiedad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='realstate.Propiedad')),
            ],
        ),
    ]
