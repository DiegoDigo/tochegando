from rest_framework import generics
from ..models import Parent, Child, School
from .serializers import SerializerParents, SerializerChild, SerializerSchool


class Parents(generics.ListAPIView):
    queryset = Parent.objects.all()
    serializer_class = SerializerParents


class Children(generics.ListAPIView):
    queryset = Child.objects.all()
    serializer_class = SerializerChild


class Schools(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SerializerSchool
