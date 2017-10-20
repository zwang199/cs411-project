# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0004_auto_20171019_0241'),
    ]

    operations = [
       # migrations.RemoveField(
       #     model_name='ingredient',
       #     name='Creator_id',
       # ),
       # migrations.RemoveField(
       #     model_name='meals',
       #     name='Creator_id',
       # ),
       # migrations.RemoveField(
       #     model_name='recipes',
       #     name='Creator_id',
       # ),
        migrations.AddField(
            model_name='ingredient',
            name='creator',
            field=models.CharField(default='admin', max_length=50),
        ),
        migrations.AddField(
            model_name='meals',
            name='creator',
            field=models.CharField(default='admin', max_length=50),
        ),
        migrations.AddField(
            model_name='recipes',
            name='creator',
            field=models.CharField(default='admin', max_length=50),
        ),
    ]