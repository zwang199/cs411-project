# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 21:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0007_like_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='snack',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='vege',
        ),
        migrations.RemoveField(
            model_name='recipes',
            name='vege',
        ),
    ]
