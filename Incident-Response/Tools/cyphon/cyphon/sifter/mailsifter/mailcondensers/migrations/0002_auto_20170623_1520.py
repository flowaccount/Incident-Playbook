# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 19:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailcondensers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailcondenser',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='mailparser',
            options={'ordering': ['name']},
        ),
    ]