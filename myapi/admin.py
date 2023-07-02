from django.contrib import admin
from .models import station, weather_data


admin.site.register(station)
admin.site.register(weather_data)
# Register your models here.
