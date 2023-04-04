from abc import ABC

from core.dataclasses.auto_park_dataclasses import AutoPark

from rest_framework.serializers import ModelSerializer, RelatedField, StringRelatedField

from .models import CarModel


class AutoParkSerializer(RelatedField, ABC):
    def to_representation(self, value: AutoPark):
        return {'id': value.id, 'name': value.name}


class CarSerializer(ModelSerializer):
    auto_park = AutoParkSerializer(read_only=True)

    class Meta:
        model = CarModel
        fields = ('id', 'car_brand', 'year', 'created_at', 'updated_at', 'auto_park', 'photo')
        read_only_fields = ('auto_park',)
        # depth = 2
