from django.contrib import admin
from .models import Airport
# Register your models here.

@admin.register(Airport)

class AirportAdmin(admin.ModelAdmin):

    list_display = [
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
        'date_created' ]
        
    list_filter = ['date_created', 'created_by', 'name', 'iso_country']
    search_fields = ('date_created', 'created_by', 'name', 'iso_country')


