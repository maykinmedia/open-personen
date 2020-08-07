from rest_framework.test import APITestCase

from openpersonen.api.test_data import test_data


class TestGetIngeschrevenPersoon(APITestCase):

    def test_list_ingeschreven_persoon(self):
        response = self.client.get('/openpersonen/api/ingeschrevenpersoon')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['burgerservicenummer'], test_data[0]['burgerservicenummer'])

    def test_retrieve_ingeschreven_persoon(self):
        test_pk = 1
        response = self.client.get(f'/openpersonen/api/ingeschrevenpersoon/{test_pk}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['burgerservicenummer'], test_data[0]['burgerservicenummer'])
