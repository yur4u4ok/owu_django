from django.db import models

from core.services.upload_car_service import upload_to

from apps.autoparks.models import AutoParkModel
from apps.cars.managers import CarManager


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
        ordering = ("id", )

    car_brand = models.CharField(max_length=20)
    year = models.IntegerField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    photo = models.ImageField(upload_to=upload_to, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = CarManager.as_manager()
