from abc import ABC

from rest_framework.serializers import ModelSerializer, RelatedField

from apps.cars.models import CarModel

from core.dataclasses.auto_park_dataclasses import AutoPark


class AutoParkSerializer(RelatedField):
    def to_representation(self, value: AutoPark):
        return {'id': value.id, 'name': value.name}


class CarSerializer(ModelSerializer):
    auto_park = AutoParkSerializer(read_only=True)

    class Meta:
        model = CarModel
        fields = ('id', 'car_brand', 'year', 'created_at', 'updated_at', 'auto_park', 'photo')
        read_only_fields = ('auto_park',)
        # depth = 2
