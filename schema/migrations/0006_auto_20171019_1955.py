# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0005_auto_20171019_0304'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='rating_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipes',
            name='rating_num',
            field=models.IntegerField(default=0),
        ),
    ]