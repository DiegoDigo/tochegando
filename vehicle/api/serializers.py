from rest_framework.serializers import ModelSerializer
from ..models import Vehicle, Driver
from profile.api.serializers import SerializerCity, SerializerSchool


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"

    def to_representation(self, instance):
        representation = super(VehicleSerializer, self).to_representation(instance)
        representation['image'] = instance.image.url
        return representation


class DriverSerializer(ModelSerializer):

    vehicle = VehicleSerializer(many=True)
    school = SerializerSchool()
    city = SerializerCity()

    class Meta:
        model = Driver
        fields = "__all__"