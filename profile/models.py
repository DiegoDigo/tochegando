from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from model_utils.models import TimeStampedModel

from utils.util import verificar_idade

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
    age = models.PositiveIntegerField(u'idade', null=True, blank=True)
    period = models.CharField(choices=periodos, max_length=10)
    image = CloudinaryField('image', blank=True, null=True)
    school = models.ForeignKey(School)

    def __str__(self):
        return self.fullname

    def save(self):
        self.age = verificar_idade(self.birthday)
        super(Child, self).save()

    class Meta:
        verbose_name = u'filho'
        verbose_name_plural = u'filhos'


class Parent(TimeStampedModel):
    user = models.ForeignKey(User, default=User, related_name='Usuario')
    fullname = models.CharField(u'nome', max_length=50)
    email = models.EmailField(verbose_name=u'Email')
    publicPlace = models.CharField(verbose_name=u'Logradouro', max_length=100)
    numberPublicPlace = models.CharField(verbose_name=u'Logradouro Numero', max_length=10)
    prefixNumber = models.CharField(u'DDD', max_length=2, null=True, blank=True)
    contactNumber = models.CharField(verbose_name=u'Numero Fixo', max_length=8, null=True, blank=True)
    prefixmobile = models.CharField(u'DDD', max_length=2)
    contactNumberMobiel = models.CharField(verbose_name=u'Numero Celular', max_length=9)
    child = models.ManyToManyField(Child, related_name='filhos', verbose_name="Filhos")
    image = CloudinaryField('image', blank=True, null=True)
    city = models.ForeignKey(City, verbose_name="Cidade")

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = u'Responsavel'
        verbose_name_plural = u'Responsaveis'
        ordering = ['fullname', 'city']



