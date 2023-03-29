from rest_framework import serializers

from .models import AutoParkModel
from ..cars.serializers import CarSerializer


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'cars', 'user')
        read_only_fields = ('user',)