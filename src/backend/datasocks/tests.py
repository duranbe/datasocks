from django.test import Client
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status
from unittest import skip
import json

# See https://developer.mozilla.org/en-US/docs/Web/HTTP/Status for correct status code


class NoAuthTest(TestCase):
    """"
    Test suite to ensure everything is Auth-protected
    """
    fixtures = ["fixture_users.yaml","fixture_dashboard.yaml"]

    def test_get_dashboard_api(self):
        client = Client()
        response = client.get('/api/1/dashboards/1/')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_get_cards_api(self):
        client = Client()
        response = client.get('/api/1/cards/1/')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_get_buttons_api(self):
        client = Client()
        response = client.get('/api/1/buttons/1/')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_get_graphs_api(self):
        client = Client()
        response = client.get('/api/1/graphs/1/')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_get_data_api(self):
        client = Client()
        response = client.get('/api/1/data/')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

class User1Test(TestCase):
    fixtures = ["fixture_users.yaml","fixture_dashboard.yaml"]

    def setUp(self):
        self.token = Token.objects.get(user__email='user1@test.com')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_dashboard_1(self):
        response = self.client.get('/api/1/dashboards/1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_get_dashboard_2(self):
        response = self.client.get('/api/1/dashboards/2/')
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)
    
    def test_get_card_1(self):
        response = self.client.get('/api/1/cards/1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_get_card_2(self):
        response = self.client.get('/api/1/cards/2/')
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

    def test_get_card_list(self):
        response = self.client.get('/api/1/cards/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        with open("datasocks/fixtures/cards_list_1.json") as json_fixture:
            self.assertEquals(json.load(json_fixture),json.loads(response.content))
        
    