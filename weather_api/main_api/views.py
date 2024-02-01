from django.shortcuts import render
from django.views import View
from .models import Country, City

from django.http import HttpResponse


#
# import openmeteo_requests
#
# import requests_cache
# import pandas as pd
# from retry_requests import retry


class MainPageView(View):
    @staticmethod
    def get(request):
        countries = Country.objects.all()
        return render(request, template_name='main_api/main_page/main_page.html', context={'countries': countries})


class CitiesPageView(View):

    @staticmethod
    def get(request, country_id):
        cities = City.objects.filter(country=country_id)
        return render(request, template_name='main_api/cities_page/cities_page.html', context={'cities': cities})


class CitiesChooseParams(View):
    @staticmethod
    def get(request, *args, **kwargs):
        params = ["Temperature (2 m)", "Temperature (120 m)", "Relative Humidity (2 m)", "Rain", "Snowfall",
                  "Snow Depth", "Cloud Cover", "Visibility", "Wind Speed (10 m)", "Wind Speed (180 m)",
                  "Wind Direction (10 m)", "Wind Direction (180 m)"]

        return render(request, template_name="main_api/stats_params_page/stats_params_page.html",
                      context={'params': params})


class CityStatistics(View):
    weather_params = {
        "Temperature (2 m)": "temperature_2m",
        "Temperature (120 m)": "temperature_120m",
        "Relative Humidity (2 m)": "relative_humidity_2m",
        "Rain": "rain",
        "Snowfall": "snowfall",
        "Snow Depth": "snow_depth",
        "Cloud Cover": "cloud_cover",
        "Visibility": "visibility",
        "Wind Speed (10 m)": "wind_speed_10m",
        "Wind Speed (180 m)": "wind_speed_180m",
        "Wind Direction (10 m)": "wind_direction_10m",
        "Wind Direction (180 m)": "wind_direction_180m"
    }

    @staticmethod
    def post(request, city_id, country_id):
        city = City.objects.get(id=city_id)
        latitude = city.latitude
        longtitude = city.longitude
        chosen_params = request.POST.getlist("checkedValues[]")
        return HttpResponse()
