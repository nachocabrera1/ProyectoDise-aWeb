# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-03 23:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_auto_persona'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='color',
            new_name='curso',
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='modelo',
            new_name='plan',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='anno',
        ),
    ]
