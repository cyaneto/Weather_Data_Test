from rest_framework import serializers

from .models import station, weather_data

class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = station
        fields = ("id", "cod_city",  "latitude", "longitude", "name_station")

class WeatherDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = weather_data
        fields = ("id","date",'hour',"cod_city", "precipitation")