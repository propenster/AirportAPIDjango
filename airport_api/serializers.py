from rest_framework import serializers
from .models import Airport


class AirportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airport
        fields = [
        'id',
        'ident', 
        'type',
        'name',
        'latitude_deg',
        'longitude_deg',
        'elevation_ft',
        'continent',
        'iso_country',
        'iso_region',
        'municipality',
        'scheduled_service',
        'gps_code',
        'iata_code',
        'local_code',
        'home_link',
        'wikipedia_link',
        'keywords',

        'created_by',
        'date_created']