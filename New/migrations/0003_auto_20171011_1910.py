# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-11 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('New', '0002_auto_20171011_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mcontains',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='rcontains',
            name='cid2',
        ),
        migrations.AlterField(
            model_name='mcontains',
            name='MID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rcontains',
            name='RID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
