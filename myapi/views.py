
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import StationSerializer, WeatherDataSerializer
from .models import station, weather_data
from rest_framework.response import Response
from rest_framework import status



class StationViewSet(viewsets.ModelViewSet):
    queryset = station.objects.all().order_by('name_station')
    serializer_class =StationSerializer
    
    def delete(self, request, id=None):
        stations = station.objects.filter(id=id)
        stations.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id=None):
        stations = station.objects.filter(id=id)
        serializer = StationSerializer(stations, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class WeatherDataViewSet(viewsets.ModelViewSet):
    queryset = weather_data.objects.all().order_by('date')
    serializer_class =WeatherDataSerializer
    
    def delete(self, request, id=None):
        weathers = weather_data.objects.filter(id=id)
        weathers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id=None):
        weathers = weather_data.objects.filter(id=id)
        serializer = WeatherDataSerializer(weathers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)