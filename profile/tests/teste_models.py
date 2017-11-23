from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from model_mommy import mommy

from profile.models import City, School, Child, Parent


class TestModelSchools(TestCase):
    def setUp(self):
        self.user = mommy.make(User, username='teste', password='teste')
        self.city = mommy.make(City, state='São Paulo', uf='SP')
        self.school = mommy.make(School, nameschool="Luiza Sallete", address="Rua nicia", addressNumber="1440",
                                 city=self.city)
        self.child = mommy.make(Child, fullname='Diego', birthday=datetime.today(), age=26,
                                period='matutino', image=None, school=self.school)
        self.parent = mommy.make(Parent, user=self.user, fullname='Maria Gilda', email='teste@gmail.com',
                                 publicPlace="rua teste", numberPublicPlace='711', prefixmobile='11',
                                 contactNumberMobiel='958044062', prefixNumber=None, contactNumber=None,
                                 city=self.city, child=[self.child], image=None)

    def test_record_create_school(self):
        self.assertTrue(self.school, School)
        self.assertEquals(self.school.__str__(), self.school.nameschool)

    def test_record_create_child(self):
        self.assertTrue(self.child, Child)
        self.assertEquals(self.child.__str__(), self.child.fullname)

    def test_record_create_parent(self):
        self.assertTrue(self.parent, Parent)
        self.assertEquals(self.parent.__str__(), self.parent.fullname)
