from core.permissions.is_superuser import IsAdminUser

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer


class CarsListView(ListAPIView):
    queryset = CarModel.objects.get_auto_park_by_id(2)
    serializer_class = CarSerializer
    filterset_class = CarFilter

    # @staticmethod
    # def get(*args, **kwargs):
    #     car = CarModel.objects.all()
    #     serializer = CarSerializer(car, many=True)
    #     return Response(serializer.data, status.HTTP_200_OK)


class CarRetrieveUpdateDelete(GenericAPIView):
    queryset = CarModel.objects.all()
    permission_classes = (IsAdminUser,)

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
