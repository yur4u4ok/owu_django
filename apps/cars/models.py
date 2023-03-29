from django.db import models

from apps.autoparks.models import AutoParkModel


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    car_brand = models.CharField(max_length=20)
    year = models.IntegerField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
