from rest_framework import serializers
from ..models import Parent, Child, School, City


class SerializerCity(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class SerializerSchool(serializers.ModelSerializer):

    city = SerializerCity()

    class Meta:
        model = School
        fields = '__all__'


class SerializerChild(serializers.ModelSerializer):

    school = SerializerSchool()

    class Meta:
        model = Child
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(SerializerChild, self).to_representation(instance)
        representation['image'] = instance.image.url
        return representation


class SerializerParents(serializers.ModelSerializer):

    child = SerializerChild(many=True)
    city = SerializerCity()

    class Meta:
        model = Parent
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(SerializerParents, self).to_representation(instance)
        representation['image'] = instance.image.url
        return representation
