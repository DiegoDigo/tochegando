from django.test import TestCase
from model_mommy import mommy
from .models import Parent, Child
from datetime import datetime
from django.contrib.auth.models import User


class TestParents(TestCase):
    def setUp(self):
        self.user = mommy.make(User, username='diego.delmiro', password='@mesma1012')
        self.parent = mommy.make(Parent, user=self.user, fullname='Diego Domingos Delmiro', prefixmobile='11',
                                 mobile='958044062', prefixphone='11', phone='39831394', city='SP')

    def test_parent_creation(self):
        self.assertTrue(isinstance(self.parent, Parent))
        self.assertEquals(self.parent.__str__(), self.parent.fullname)


class TestChildren(TestCase):
    def setUp(self):
        self.user = mommy.make(User, username='diego.delmiro', password='@mesma1012')
        self.parent = mommy.make(Parent, user=self.user, fullname='Diego Domingos Delmiro', prefixmobile='11',
                                 mobile='958044062', prefixphone='11', phone='39831394', city='SP')
        self.child = mommy.make(Child, parent=self.parent, fullname='Jose Willian Domingos Almeida',
                                birthday=datetime.today().date(), age=25, period='manha')

    def test_child_creation(self):
        self.assertTrue(isinstance(self.child, Child))
        self.assertEquals(self.child.__str__(), self.child.fullname)