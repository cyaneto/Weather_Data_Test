from rest_framework import serializers

from .models import station, weather_data

class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = station
        fields = ("id", "cod_city",  "latitude", "longitude", "name_station")

class WeatherDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = weather_data
        
        fields = ("id","date",'hour',"cod_city", "precipitation", "dry_bulb_temperature", "wet_bulb_temperature", "high_temperature", "low_temperature", "relative_humidity", "relative_humidity_avg", "pressure", "sea_pressure", "wind_direction", "wind_speed_avg", "cloud_cover", "evaporation" )