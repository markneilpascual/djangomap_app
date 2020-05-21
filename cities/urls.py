from django.urls import path
from cities.views import CitiesDetailView, CitiesListView, CreateCityDetail, add_detail,IndexView


app_name = 'cities'

urlpatterns = [

    # functioning
    path('CityDetailView/<int:pk>',CitiesDetailView.as_view(), name='city-detail-view'),
    # functioning
    path('CitiesListView/',CitiesListView.as_view(), name='city-list'),
    path('',IndexView.as_view(), name='index'),

    path('CityDetailView/',CreateCityDetail.as_view(), name='create-detail-view'),
    path('add/', add_detail, name='add_detail'),
]