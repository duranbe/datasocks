from django.test import Client
from django.test import TestCase

HTTP_STATUS_CODE_FORBIDDEN = 403
HTTP_STATUS_CODE_UNAUTHORIZED = 401

# Create your tests here.
class DashboardTest(TestCase):
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

    