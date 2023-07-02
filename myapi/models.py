# models.py
from django.db import models


class station(models.Model):
    name_station = models.CharField(max_length=60)
    cod_city =  models.IntegerField()
    latitude = models.FloatField()
    longitude =  models.FloatField()

    def __str__(self):
        return self.name_station
    
class weather_data(models.Model):
    date = models.DateField()
    cod_city =  models.IntegerField()
    hour =  models.IntegerField()
    precipitation = models.FloatField( null=True, blank=True)
    dry_bulb_temperature = models.FloatField( null=True, blank=True)
    wet_bulb_temperature = models.FloatField( null=True, blank=True)
    high_temperature = models.FloatField( null=True, blank=True)
    low_temperature = models.FloatField( null=True, blank=True)
    relative_humidity = models.FloatField( null=True, blank=True)
    relative_humidity_avg = models.FloatField( null=True, blank=True)
    pressure = models.FloatField( null=True, blank=True)
    sea_pressure = models.FloatField( null=True, blank=True)
    wind_direction = models.FloatField( null=True, blank=True)
    wind_speed_avg = models.FloatField( null=True, blank=True)
    cloud_cover = models.FloatField( null=True, blank=True)
    evaporation = models.FloatField( null=True, blank=True)
    
    def __str__(self):
        return self.date