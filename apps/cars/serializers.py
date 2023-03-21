from rest_framework import serializers

from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'car_brand', 'year', 'seats_count', 'body_type', 'engine_volume')
