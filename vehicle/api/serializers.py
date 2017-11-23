from rest_framework.serializers import ModelSerializer
from ..models import Vehicle, Driver
from profile.api.serializers import SerializerCity, SerializerSchool, SerializerParents


class VehicleSerializer(ModelSerializer):
    parents = SerializerParents(many=True)

    class Meta:
        model = Vehicle
        fields = "__all__"


class DriverSerializer(ModelSerializer):
    vehicle = VehicleSerializer()
    school = SerializerSchool()
    city = SerializerCity()

    class Meta:
        model = Driver
        fields = "__all__"

    def to_representation(self, instance):
        representation = super(DriverSerializer, self).to_representation(instance)
        representation['image'] = instance.image.url
        return representation
