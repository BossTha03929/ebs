from django.db import models
from pandas import period_range

# Create your models here.
class Parameter(models.Model):
    period = models.DecimalField(decimal_places=20, max_digits=50)
    primary_mass = models.DecimalField(decimal_places=20, max_digits=50)
    primary_radius = models.DecimalField(decimal_places=20, max_digits=50)
    primary_luminosity = models.DecimalField(decimal_places=20, max_digits=50)
    primary_temperature = models.DecimalField(decimal_places=20, max_digits=50)
    secondary_mass = models.DecimalField(decimal_places=20, max_digits=50)
    secondary_radius = models.DecimalField(decimal_places=20, max_digits=50)
    secondary_luminosity = models.DecimalField(decimal_places=20, max_digits=50)
    secondary_temperature = models.DecimalField(decimal_places=20, max_digits=50)
    mass_ratio = models.DecimalField(decimal_places=20, max_digits=50)

    class Meta:
        db_table = 'EBs_Data'

class Mcl(models.Model):
    aa = models.TextField()
