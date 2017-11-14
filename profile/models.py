from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

cidades = (('SP', 'São Paulo'),
           ('RJ', 'Rio de Janeiro'),
           ('MG', 'Minas Gerais'), )


periodos = (('manha', 'Matutino'),
            ('tarde', 'Diurno'),)


class School(models.Model):
    nameschool = models.CharField(u'Nome Escola', max_length=100)
    address = models.CharField(u'Endereço', max_length=100)
    addressNumber = models.CharField(u'Numero', max_length=4)

    def __str__(self):
        return self.nameschool

    class Meta:
        verbose_name = u'escola'
        verbose_name_plural = u'escolas'


class Child(models.Model):
    fullname = models.CharField(u'nome', max_length=50)
    birthday = models.DateField(u'data nascimento')
    age = models.PositiveIntegerField(u'idade')
    period = models.CharField(choices=periodos, max_length=10)
    image = CloudinaryField(u'imagem')
    school = models.ForeignKey(School)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = u'filho'
        verbose_name_plural = u'filhos'


class Parent(models.Model):
    user = models.ForeignKey(User, default=User, related_name='Usuario')
    fullname = models.CharField(u'nome', max_length=50)
    prefixmobile = models.CharField(u'DDD', max_length=2)
    mobile = models.CharField(u'celular', max_length=9)
    prefixphone = models.CharField(u'DDD', max_length=2, null=True, blank=True)
    phone = models.CharField(u'telefone', max_length=8, null=True, blank=True)
    city = models.CharField(u'cidade', choices=cidades, max_length=50)
    child = models.ManyToManyField(Child, related_name='filhos')
    image = CloudinaryField('imagem')

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = u'pais'
        verbose_name_plural = u'pais'
        ordering = ['fullname', 'city']



