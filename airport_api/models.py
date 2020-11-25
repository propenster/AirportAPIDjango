from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# "id":5336,
# "ident":"PAAQ",
# "type":"medium_airport",
# "name":"Warren \"Bud\" Woods Palmer Municipal Airport",
# "latitude_deg":61.5948980000000000000000,
# "longitude_deg":-149.089010000000000000,
# "elevation_ft":242,
# "continent":"NA",
# "iso_country":"US",
# "iso_region":"US-AK",
# "municipality":"Palmer",
# "scheduled_service":"no",
# "gps_code":"PAAQ",
# "iata_code":"PAQ",
# "local_code":"PAQ",
# "home_link":null,
# "wikipedia_link":"https://en.wikipedia.org/wiki/Palmer_Municipal_Airport",
# "keywords":"Palmer Muni, Palmer Buddy Woods Municipal"

class Airport(models.Model):
    ident = models.CharField(max_length=7)
    type = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    latitude_deg = models.CharField(max_length=30)
    longitude_deg = models.CharField(max_length=30)
    elevation_ft = models.DecimalField(decimal_places=5, max_digits=10)
    continent = models.CharField(max_length=30)
    iso_country = models.CharField(max_length=2)
    iso_region = models.CharField(max_length=10)
    municipality = models.CharField(max_length=100)
    scheduled_service = models.CharField(max_length=30)
    gps_code = models.CharField(max_length=10)
    iata_code = models.CharField(max_length=10)
    local_code = models.CharField(max_length=10)
    home_link = models.URLField(null=True)
    wikipedia_link = models.URLField()
    keywords = models.CharField(max_length=100, null=True)

    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created', 'created_by', 'name', 'iso_country']

    def __str__(self):
        return self.name


