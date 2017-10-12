# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-11 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('IID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('snack', models.BooleanField(default=False)),
                ('vege', models.BooleanField(default=False)),
                ('calories', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('sodium', models.IntegerField()),
                ('CreatorID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mcontains',
            fields=[
                ('MID', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('MID', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=50)),
                ('rating', models.DecimalField(decimal_places=3, max_digits=4)),
                ('calories', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('sodium', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rcontains',
            fields=[
                ('RID', models.IntegerField(primary_key=True, serialize=False)),
                ('IIDS', models.ManyToManyField(to='New.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('RID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('vege', models.BooleanField(default=False)),
                ('rating', models.DecimalField(decimal_places=3, max_digits=4)),
                ('description', models.TextField()),
                ('calories', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('sodium', models.IntegerField()),
                ('CreatorID', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='mcontains',
            name='RIDs',
            field=models.ManyToManyField(to='New.Recipes'),
        ),
        migrations.AddField(
            model_name='mcontains',
            name='Snacks',
            field=models.ManyToManyField(to='New.Ingredient'),
        ),
    ]
