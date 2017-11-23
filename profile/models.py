from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from model_utils.models import TimeStampedModel


periodos = (('manha', 'Matutino'),
            ('tarde', 'Diurno'),)


class City(models.Model):
    state = models.CharField(u'Estado', max_length=100)
    uf = models.CharField(u'UF', max_length=2)

    def __str__(self):
        return self.state

    class Meta:
        verbose_name = u'cidade'
        verbose_name_plural = u'cidades'
        ordering = ['uf', 'state']


class School(models.Model):
    nameschool = models.CharField(u'Nome Escola', max_length=100)
    address = models.CharField(u'Endereço', max_length=100)
    addressNumber = models.CharField(u'Numero', max_length=4)
    city = models.ForeignKey(City)

    def __str__(self):
        return self.nameschool

    class Meta:
        verbose_name = u'escola'
        verbose_name_plural = u'escolas'


class Child(TimeStampedModel):
    fullname = models.CharField(u'nome', max_length=50)
    birthday = models.DateField(u'data nascimento')
    age = models.PositiveIntegerField(u'idade')
    period = models.CharField(choices=periodos, max_length=10)
    image = CloudinaryField('image', blank=True, null=True)
    school = models.ForeignKey(School)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = u'filho'
        verbose_name_plural = u'filhos'


class Parent(TimeStampedModel):
    user = models.ForeignKey(User, default=User, related_name='Usuario')
    fullname = models.CharField(u'nome', max_length=50)
    prefixmobile = models.CharField(u'DDD', max_length=2)
    mobile = models.CharField(u'celular', max_length=9)
    prefixphone = models.CharField(u'DDD', max_length=2, null=True, blank=True)
    phone = models.CharField(u'telefone', max_length=8, null=True, blank=True)
    child = models.ManyToManyField(Child, related_name='filhos')
    image = CloudinaryField('image', blank=True, null=True)
    city = models.ForeignKey(City)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = u'Responsavel'
        verbose_name_plural = u'Responsaveis'
        ordering = ['fullname', 'city']



