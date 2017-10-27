from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

cidades = (('SP', 'São Paulo'),
           ('RJ', 'Rio de Janeiro'),
           ('MG', 'Minas Gerais'), )


periodos = (('manha', 'Matutino'),
            ('tarde', 'Diurno'),)


class Parent(models.Model):
    user = models.ForeignKey(User, default=User, related_name='Usuario')
    fullname = models.CharField(u'nome', max_length=50)
    prefixmobile = models.CharField(u'DDD', max_length=2)
    mobile = models.CharField(u'celular', max_length=9)
    prefixphone = models.CharField(u'DDD', max_length=2, null=True, blank=True)
    phone = models.CharField(u'telefone', max_length=8, null=True, blank=True)
    city = models.CharField(u'cidade', choices=cidades, max_length=50)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = u'pais'
        verbose_name_plural = u'pais'
        ordering = ['fullname', 'city']


class Child(models.Model):
    parent = models.ForeignKey(Parent, default=Parent.user, related_name='pais')
    fullname = models.CharField(u'nome', max_length=50)
    birthday = models.DateField(u'data nascimento')
    age = models.PositiveIntegerField(u'idade')
    period = models.CharField(choices=periodos, max_length=10)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = u'filho'
        verbose_name_plural = u'filhos'