# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


import uuid

# Create your models here.
#class User(models.Model):
#    ID = models.IntegerField(primary_key=True)
#    username = models.CharField(max_length=20)
#    email = models.EmalField()
#    password = models.CharField(max_length=50)
#    followers = models.ManyToManyField("self")
#    follower_num = models.IntegerField(default=0)



class Ingredient(models.Model):
    iid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    calories = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    sodium = models.IntegerField()
    creator = models.CharField(max_length = 50, default = 'admin')

    def _str_(self):
        return self.name

    def get_id(self):
        return self.iid

class Recipes(models.Model):
    rid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    rating = models.DecimalField(decimal_places=3, max_digits=4)
    rating_num = models.IntegerField(default = 0)
    calories = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    sodium = models.IntegerField()
    creator = models.CharField(max_length = 50, default = 'admin')

    def _str_(self):
        return self.name

    def get_id(self):
        return self.rid



class Meals(models.Model):
    mid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=255)
    rating = models.DecimalField(decimal_places=3, max_digits=4)
    rating_num = models.IntegerField(default = 0)
    calories = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    sodium = models.IntegerField()
    creator = models.CharField(max_length = 50, default = 'admin')

class like_recipe(models.Model):
    user_id = models.ForeignKey(User, null = True)
    r_id = models.ForeignKey(Recipes, null = True)

class Recipes_detail(models.Model):
    r_id = models.ForeignKey(Recipes)
    instructions = models.TextField()

class Recipes_tag(models.Model):
    detail = models.CharField(max_length=50)
    def get_info(self):
        ret = "id: " + self.id + "\ndetail: " + self.detail
        return ret;

class contain_tag(models.Model):
    r_id = models.ForeignKey(Recipes, null = True)
    t_id = models.ForeignKey(Recipes_tag, null = True)

class Recipes_HitCount(models.Model):
    recipe = models.ForeignKey(Recipes, null = True)
    hitcount = models.IntegerField(default = 0)

class Recipes_Comment(models.Model):
    user = models.ForeignKey(User, null = True)
    recipe = models.ForeignKey(Recipes, null = True)
    rating = models.DecimalField(decimal_places=3, max_digits=4)
    comment = models.TextField()
    up_vote = models.IntegerField(default = 0)
    down_vote = models.IntegerField(default = 0)
    creat_time = models.DateTimeField(default=timezone.now)




