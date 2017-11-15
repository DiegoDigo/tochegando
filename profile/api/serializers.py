from rest_framework import serializers
from ..models import Parent, Child, School


class SerializerSchool(serializers.ModelSerializer):
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

    class Meta:
        model = Parent
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(SerializerParents, self).to_representation(instance)
        representation['image'] = instance.image.url
        return representation
