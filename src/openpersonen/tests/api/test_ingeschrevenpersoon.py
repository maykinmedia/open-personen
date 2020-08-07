from rest_framework.test import APITestCase


class TestGetIngeschrevenPersoon(APITestCase):

    def test_list_ingeschreven_persoon(self):
        response = self.client.get('/openpersonen/api/ingeschrevenpersonen')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, 'In list')

    def test_retrieve_ingeschreven_persoon(self):
        test_pk = 1
        response = self.client.get(f'/openpersonen/api/ingeschrevenpersonen/{test_pk}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, f'In retrieve, burgerservicenummer is {test_pk}')
