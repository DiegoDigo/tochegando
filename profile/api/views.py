from rest_framework import generics
from ..models import Parent, Child
from .serializers import SerializerParents, SerializerChild


class Parents(generics.ListAPIView):
    queryset = Parent.objects.all()
    serializer_class = SerializerParents


class Children(generics.ListAPIView):
    queryset = Child.objects.all()
    serializer_class = SerializerChild
