from rest_framework import serializers
from ..models import Parent, Child


class SerializerChild(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'


class SerializerParents(serializers.ModelSerializer):

    child = SerializerChild(many=True)

    class Meta:
        model = Parent
        fields = '__all__'
