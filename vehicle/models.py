from __future__ import unicode_literals
from django.db import models
from profile.models import School, City

typesVehicle = (('micro', 'Micro-Onibus'),
                ('min', 'Mini-Van'),)


class Vehicle(models.Model):
    typevehicle = models.CharField(u'Tipo Veiculo', choices=typesVehicle, max_length=10)
    capacity = models.PositiveIntegerField(u'Capacidade')
    isDeficiente = models.BooleanField(u'Deficiente', default=False)

    def __str__(self):
        return self.typevehicle

    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'


class Driver(models.Model):
    fullname = models.CharField(u'nome', max_length=100)
    category = models.CharField(u'Categoria', max_length=3)
    vehicle = models.ManyToManyField(Vehicle, related_name='veiculos')
    school = models.ForeignKey(School)
    cidade = models.ForeignKey(City)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'