from __future__ import unicode_literals
from django.db import models
from profile.models import School, City, Parent
from .querys import DriversQuerySet
from cloudinary.models import CloudinaryField
from model_utils.models import TimeStampedModel


typesVehicle = (('micro', 'Micro-Onibus'),
                ('min', 'Mini-Van'),)


class Vehicle(models.Model):
    typevehicle = models.CharField(u'Tipo Veiculo', choices=typesVehicle, max_length=10)
    isDeficiente = models.BooleanField(u'Deficiente', default=False)
    capacity = models.PositiveIntegerField(default=50)
    parents = models.ManyToManyField(Parent, related_name="parents", verbose_name=u'Pais')

    def __str__(self):
        return self.typevehicle

    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'


class Driver(TimeStampedModel):
    fullname = models.CharField(u'nome', max_length=100)
    email = models.EmailField(verbose_name=u'E-mail')
    contactNumberDDD = models.CharField(verbose_name=u'DDD', max_length=5)
    contactNumber = models.CharField(verbose_name=u'Numero Fixo', max_length=8, null=True, blank=True)
    contactNumberMobile = models.CharField(verbose_name=u'Numero Celular', max_length=9)
    categoryHab = models.CharField(verbose_name=u'Categoria Habilitação', max_length=2)
    vehicle = models.ForeignKey(Vehicle, related_name='veiculos', verbose_name="veiculo")
    city = models.ForeignKey(City, verbose_name="Cidade")
    createdIn = models.DateField(auto_now=True, auto_now_add=False)
    image = CloudinaryField(u'imagem')
    objects = DriversQuerySet.as_manager()

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'