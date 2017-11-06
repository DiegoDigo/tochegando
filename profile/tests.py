import logging

from unittest.mock import Mock, patch
from django.db import DatabaseError
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Parent


class TestParents(TestCase):

    cursor_wrapper = Mock()
    cursor_wrapper.side_effect = DatabaseError

    def setUp(self):
        self.client = APIClient()
        logging.disable(logging.CRITICAL)

    def teste_get_200(self):
        response = self.client.get('/api/parents/')
        self.assertEqual(200, response.status_code)

    @patch.object(Parent.objects,'all')
    def teste_get_200_return_without_data(self, all):
        response = self.client.get('/api/parents/')
        all.return_value = None
        self.assertNotEqual(response.data, all())

