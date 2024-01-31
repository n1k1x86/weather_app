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
