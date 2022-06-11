from django.test import Client
from django.test import TestCase

HTTP_STATUS_CODE_FORBIDDEN = 403

# Create your tests here.
class DashboardTest(TestCase):
    fixtures = ["fixture.yaml"]

    def test_get_dashboard_api(self):
        client = Client()
        response = client.get('/api/1/dashboards/1/')
        self.assertEqual(response.status_code,HTTP_STATUS_CODE_FORBIDDEN)