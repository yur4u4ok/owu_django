from rest_framework import serializers

from apps.cars.serializers import CarSerializer
from apps.autoparks.models import AutoParkModel


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'user', 'cars')
        read_only_fields = ('user',)
