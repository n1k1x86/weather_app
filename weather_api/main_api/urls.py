from django.urls import path
from .views import MainPageView, CitiesPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('country/<int:country_id>/', CitiesPageView.as_view(), name='cities_page')
]
