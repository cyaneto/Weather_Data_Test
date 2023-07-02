# Generated by Django 4.2.2 on 2023-07-02 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_weather_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather_data',
            name='cloud_cover',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='dry_bulb_temperature',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='evaporation',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='high_temperature',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='low_temperature',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='precipitation',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='pressure',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='relative_humidity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='relative_humidity_avg',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='sea_pressure',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='wet_bulb_temperature',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='wind_direction',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='wind_speed_avg',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
