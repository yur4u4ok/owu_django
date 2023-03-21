from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import CarModel
from .serializers import CarSerializer


class CarsGetPost(APIView):

    @staticmethod
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarSerializer(instance=cars, many=True)
        cars = [{'id': car['id'], 'car_brand': car['car_brand'], 'year': car['year']} for car in serializer.data]
        return Response(cars, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class CarGetUpdateDelete(APIView):

    @staticmethod
    def get(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response('not found', status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(instance=car)

        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        data = self.request.data
        pk = kwargs['pk']

        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response('not found', status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(car, data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data

        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response('not found', status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(car, data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    @staticmethod
    def delete(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response('not found', status.HTTP_404_NOT_FOUND)

        car.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
