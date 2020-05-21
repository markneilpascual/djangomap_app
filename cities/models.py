from django.db import models
from django.contrib.gis.db import models as geomodels


class City(models.Model):
    name = models.CharField(max_length=100, blank=False)
    geometry = geomodels.PointField()

    class Meta:
        # order of drop-down list items
        ordering = ('name',)

        # plural form in admin view
        verbose_name_plural = 'cities'

class City_Detail(models.Model):
    city = models.ForeignKey('City',related_name='city_details', on_delete=models.CASCADE)
    city_detail = models.CharField(max_length=255)
    geometry = geomodels.PointField(srid=4326)


    class Meta:
        ordering = ('city',)