from rest_framework import generics
from ..models import Vehicle, Driver
from .serializers import DriverSerializer, VehicleSerializer


class Drivers(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class Vehicles(generics.ListAPIView):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        return Vehicle.objects.filter(id=self.kwargs['pk'])