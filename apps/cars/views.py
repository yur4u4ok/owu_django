from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import CarModel
from .serializers import CarSerializer


class CarsGetPost(GenericAPIView):

    @staticmethod
    def get(self, *args, **kwargs):
        car = CarModel.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class CarRetrieveUpdateDelete(GenericAPIView):
    queryset = CarModel.objects.all()

    def get(self, *args, **kwargs):
        car = self.get_object()
        serializer = CarSerializer(car)

        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        data = self.request.data

        car = self.get_object()
        serializer = CarSerializer(car, data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        car = self.get_object()
        car.delete()

        return Response(status.HTTP_204_NO_CONTENT)
