from django.db import models


class Location(models.Model):
    city = models.CharField(default=None, max_length=255)
    country = models.CharField(default=None, max_length=255)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    class Meta:
        db_table = 'location'
