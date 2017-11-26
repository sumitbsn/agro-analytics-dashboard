from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Cropdata(models.Model):
    state = models.CharField(db_column='State', max_length=20)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=30)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    season = models.CharField(db_column='Season', max_length=11)  # Field name made lowercase.
    crop = models.CharField(db_column='Crop', max_length=25)  # Field name made lowercase.
    production = models.IntegerField(db_column='Production')  # Field name made lowercase.
    productivity = models.DecimalField(db_column='Productivity', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cropdata'




