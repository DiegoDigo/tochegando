from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class TestApi(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_schools_success_status_code(self):
        response = self.client.get(reverse("api:school"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_parent_success_status_code(self):
        response = self.client.get(reverse("api:parent"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_child_success_status_code(self):
        response = self.client.get(reverse("api:child"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
