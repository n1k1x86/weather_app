import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry


def process_data(response, chosen_params):
    hourly = response.Hourly()
    hourly_data = {"date": pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s"),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s"),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    )}
    for ind, param in enumerate(chosen_params):
        hourly_data[param] = hourly.Variables(ind).ValuesAsNumpy()

    return pd.DataFrame(data=hourly_data)


def get_weather_data(latitude, longitude, chosen_params):
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": chosen_params,
        "timezone": "auto"
    }

    response = openmeteo.weather_api(url, params=params)[0]
    hourly_dataframe = process_data(response, chosen_params)
    return hourly_dataframe
