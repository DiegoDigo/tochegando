from django.test import TestCase
from model_mommy import mommy
from .models import Parent
from django.contrib.auth.models import User


class TestGenre(TestCase):
    def setUp(self):
        self.user = mommy.make(User, username='diego.delmiro', password='@mesma1012')
        self.parent = mommy.make(Parent, user=self.user, fullname='Diego Domingos Delmiro', prefixmobile='11',
                                 mobile='958044062', prefixphone='11', phone='39831394', city='SP')

    def test_genre_creation(self):
        self.assertTrue(isinstance(self.parent, Parent))
        self.assertEquals(self.parent.__str__(), self.parent.fullname)
