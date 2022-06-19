from django.test import Client
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

HTTP_STATUS_CODE_FORBIDDEN = 403
HTTP_STATUS_CODE_UNAUTHORIZED = 401

HTTPS_STATUS_CODE_SUCCESS = 200

# Create your tests here.
class NoAuthTest(TestCase):
    fixtures = ["fixture.yaml"]

    def test_get_dashboard_api(self):
        client = Client()
        response = client.get('/api/1/dashboards/1/')
        self.assertEqual(response.status_code,HTTP_STATUS_CODE_UNAUTHORIZED)

    def test_get_cards_api(self):
        client = Client()
        response = client.get('/api/1/cards/1/')
        self.assertEqual(response.status_code,HTTP_STATUS_CODE_UNAUTHORIZED)

    def test_get_buttons_api(self):
        client = Client()
        response = client.get('/api/1/buttons/1/')
        self.assertEqual(response.status_code,HTTP_STATUS_CODE_UNAUTHORIZED)

    def test_get_graphs_api(self):
        client = Client()
        response = client.get('/api/1/graphs/1/')
        self.assertEqual(response.status_code,HTTP_STATUS_CODE_UNAUTHORIZED)

    def test_get_data_api(self):
        client = Client()
        response = client.get('/api/1/data/')
        self.assertEqual(response.status_code,HTTP_STATUS_CODE_UNAUTHORIZED)

class User1Test(TestCase):

    fixtures = ["fixture.yaml"]

    def setUp(self):
        token = Token.objects.get(user__email='user1@test.com')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_get_dashboard_1(self):
        response = self.client.get('/api/1/dashboards/1/')
        self.assertEqual(response.status_code,HTTPS_STATUS_CODE_SUCCESS)