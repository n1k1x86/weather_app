from django.urls import path
from .views import MainPageView, CitiesPageView, CitiesChooseParams, CityStatistics

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('country/<int:country_id>/', CitiesPageView.as_view(), name='cities_page'),
    path('country/<int:country_id>/city/<int:city_id>/choose_params/', CitiesChooseParams.as_view(),
         name='choose_params'),
    path('country/<int:country_id>/city/<int:city_id>/choose_params/built_statistics/', CityStatistics.as_view(),
         name='choose_params'),
]
