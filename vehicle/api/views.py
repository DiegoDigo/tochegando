from rest_framework import generics
from ..models import Vehicle, Driver
from .serializers import DriverSerializer, VehicleSerializer


class Drivers(generics.ListAPIView):
    serializer_class = DriverSerializer

    def get_queryset(self):
        city = self.request.GET.get("city")
        school = self.request.GET.get("school")
        if city:
            return Driver.objects.get_driver_by_city(self.request.GET.get("city"))
        if school:
            return Driver.objects.get_driver_by_school(self.request.GET.get("school"))
        return Driver.objects.all()


class Vehicles(generics.ListAPIView):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        return Vehicle.objects.filter(id=self.kwargs['pk'])

