from django.test import TestCase

from openpersonen.api.client import Client


class TestClient(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_gezinssituatie_op_adres_aanvrager(self):
        test_bsn = 123456789

        response = self.client.get_gezinssituatie_op_adres_aanvrager(test_bsn)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'antwoord')

    def test_get_kinderen_van_aanvrager(self):
        test_bsn = 123456789

        response = self.client.get_kinderen_van_aanvrager(test_bsn)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'antwoord')

    def test_get_natuurlijk_persoon(self):
        test_bsn = 123456789

        response = self.client.get_natuurlijk_persoon(test_bsn)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'antwoord')

    def test_get_vestiging(self):
        test_bsn = 123456789

        response = self.client.get_vestiging(test_bsn)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'antwoord')
