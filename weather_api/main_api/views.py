from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry


class MainPageView(View):
    def get(self, request):

        cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
        retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
        openmeteo = openmeteo_requests.Client(session=retry_session)

        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": 43.1056,
            "longitude": 131.8735,
            "hourly": "temperature_2m"
        }
        responses = openmeteo.weather_api(url, params=params)
        response = responses[0]

        print(f"Coordinates {response.Latitude()}°E {response.Longitude()}°N")
        print(f"Elevation {response.Elevation()} m asl")
        print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
        print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

        # Process hourly data. The order of variables needs to be the same as requested.
        hourly = response.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

        hourly_data = {"date": pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s"),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s"),
            freq=pd.Timedelta(seconds=hourly.Interval()),
            inclusive="left"
        ), "temperature_2m": hourly_temperature_2m}

        hourly_dataframe = pd.DataFrame(data=hourly_data)
        print(hourly_dataframe)

        return render(request, template_name='main_api/main_page.html')
