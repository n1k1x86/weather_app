from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Country


# from django.http import HttpResponse
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
