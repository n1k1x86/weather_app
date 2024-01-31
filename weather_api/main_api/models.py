from django.db import models


class Country(models.Model):
    name = models.CharField(default=None, max_length=255)
    country_image = models.ImageField(upload_to='images/country/')
    some_info = models.CharField(max_length=255)

    class Meta:
        db_table = 'country'


class City(models.Model):
    city = models.CharField(default=None, max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_image = models.ImageField(upload_to='images/cities/')
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    class Meta:
        db_table = 'city'
