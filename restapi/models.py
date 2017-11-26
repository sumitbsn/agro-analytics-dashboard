# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Info(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info'

class Cropdata(models.Model):
    state = models.CharField(db_column='State', max_length=10)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=15)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=4)  # Field name made lowercase.
    season = models.CharField(db_column='Season', max_length=11)  # Field name made lowercase.
    crop = models.CharField(db_column='Crop', max_length=25)  # Field name made lowercase.
    production = models.CharField(db_column='Production', max_length=10)  # Field name made lowercase.
    productivity = models.CharField(db_column='Productivity', max_length=12, blank=True, null=True)  # Field name made lowercase.
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cropdata'

