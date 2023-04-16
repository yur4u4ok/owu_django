from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer

from core.permissions.is_superuser import IsAdminUser


class CarsListView(ListAPIView):
    # queryset = CarModel.objects.get_auto_park_by_id(2)
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter

    # @staticmethod
    # def get(*args, **kwargs):
    #     car = CarModel.objects.all()
    #     serializer = CarSerializer(car, many=True)
    #     return Response(serializer.data, status.HTTP_200_OK)


class CarRetrieveUpdateDelete(GenericAPIView):
    """
    get:
        Get car by id
    put:
        Change car by id
    patch:
        Partial change car by id
    delete:
        Delete car by id
    """

    queryset = CarModel.objects.all()
    permission_classes = (IsAdminUser,)


    def get_serializer(self):
        pass

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

    def patch(self, *args, **kwargs):
        data = self.request.data

        car = self.get_object()
        serializer = CarSerializer(car, data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        car = self.get_object()
        car.delete()

        return Response(status.HTTP_204_NO_CONTENT)
