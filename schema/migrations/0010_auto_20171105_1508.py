# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 21:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0009_auto_20171104_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructions', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='recipes',
            name='description',
        ),
        migrations.AddField(
            model_name='recipes_detail',
            name='r_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.Recipes'),
        ),
    ]
