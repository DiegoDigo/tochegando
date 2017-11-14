from rest_framework import serializers
from ..models import Parent, Child


class SerializerChild(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(SerializerChild, self).to_representation(instance)
        representation['imagem'] = instance.image.url
        return representation



class SerializerParents(serializers.ModelSerializer):

    child = SerializerChild(many=True)

    class Meta:
        model = Parent
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(SerializerParents, self).to_representation(instance)
        representation['imagem'] = instance.image.url
        return representation
