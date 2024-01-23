from django.shortcuts import render
from django.views import View


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
        return render(request, template_name='main_api/main_page/main_page.html')
