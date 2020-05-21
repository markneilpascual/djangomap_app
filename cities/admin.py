from django.contrib import admin
from django.contrib.gis import admin
from cities.models import City, City_Detail
from leaflet.admin import LeafletGeoAdmin


class CityAdmin(LeafletGeoAdmin):
    # fields to show in admin listview
    list_display = ('name', 'geometry')

class City_detailAdmin(LeafletGeoAdmin):
    list_display = ('city','city_detail','geometry')

# register models in the admin site
admin.site.register(City, CityAdmin),
admin.site.register(City_Detail, City_detailAdmin),
