from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    car_brand = models.CharField(max_length=20)
    year = models.IntegerField()
    seats_count = models.IntegerField()
    body_type = models.CharField(max_length=15)
    engine_volume = models.FloatField()
    