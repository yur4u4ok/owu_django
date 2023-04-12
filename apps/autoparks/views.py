from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from ..cars.serializers import CarSerializer
from .filters import AutoParkFilter
from .models import AutoParkModel
from .serializers import AutoParkSerializer


class AutoParkListCreateView(GenericAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @staticmethod
    def get(self, *args, **kwargs):
        auto_parks = AutoParkModel.objects.all()
        serializer = AutoParkSerializer(auto_parks, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = AutoParkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)

        return Response(serializer.data)


class AutoParkCreateListCarsView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated,)
    filterset_class = AutoParkFilter

    # def get(self, *args, **kwargs):
    #     auto_park = self.get_object()
    #     serializer = CarSerializer(auto_park.cars, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, *args, **kwargs):
    #     auto_park = self.get_object()
    #     data = self.request.data
    #
    #     serializer = CarSerializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(auto_park=auto_park)
    #
    #     return Response(serializer.data)
