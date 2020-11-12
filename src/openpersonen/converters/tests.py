from django.urls import reverse
from django.test import override_settings

from rest_framework.test import APITestCase


@override_settings(OPENPERSONEN_USE_AUTHENTICATION=False)
class TestStufbg2ApiView(APITestCase):

    def test_stuf_2_api_view(self):
        response = self.client.post(reverse('api-2-stufbg'))
        self.assertEqual(response.status_code, 200)


@override_settings(OPENPERSONEN_USE_AUTHENTICATION=False)
class TestApi2StufbgView(APITestCase):

    def test_api_2_stufbg_view(self):
        response = self.client.post(reverse('stufbg-2-api'))
        self.assertEqual(response.status_code, 200)



