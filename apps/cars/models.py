from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    car_brand = models.CharField(max_length=20)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
