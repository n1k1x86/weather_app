import json

from django.shortcuts import render
from django.views import View
from .models import Country, City

from .get_weather_data import get_weather_data


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

    weather_params_charts = {
        "temperature_2m": "Temperature (2 m)",
        "temperature_120m": "Temperature (120 m)",
        "relative_humidity_2m": "Relative Humidity (2 m)",
        "rain": "Rain",
        "snowfall": "Snowfall",
        "snow_depth": "Snow Depth",
        "cloud_cover": "Cloud Cover",
        "visibility": "Visibility",
        "wind_speed_10m": "Wind Speed (10 m)",
        "wind_speed_180m": "Wind Speed (180 m)",
        "wind_direction_10m": "Wind Direction (10 m)",
        "wind_direction_180m": "Wind Direction (180 m)"
    }

    def get(self, request, city_id, country_id):
        city = City.objects.get(id=city_id)
        latitude = city.latitude
        longitude = city.longitude
        chosen_params = list(map(lambda x: self.weather_params[x], request.GET.getlist("param")))

        dataset, current_data = get_weather_data(latitude, longitude, chosen_params)
        labels = list(dataset.columns)
        dataset['date'] = dataset['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
        chart_data = []
        dates = list(dataset['date'])

        for label in labels[1:]:
            chart_data.append({
                'label': self.weather_params_charts[label],
                'data': [{'x': dates[ind], 'y': round(data, 3)} for ind, data in
                         enumerate(list(dataset[label]))]
            })

        current_data = {self.weather_params_charts[k]: round(v, 2) for k, v in current_data.items()}

        return render(request, template_name="main_api/stats_chart_page/stats_chart_page.html",
                      context={'chart_data': json.dumps(chart_data), 'labels': labels,
                               'current_data': json.dumps(current_data)})
