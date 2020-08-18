from django.conf import settings
from django.test import TestCase

from openpersonen.api.client import Client


class TestClient(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_gezinssituatie_op_adres_aanvrager(self):
        test_bsn = 123456789

        response = self.client.get_gezinssituatie_op_adres_aanvrager(test_bsn)

        self.assertEqual(response.status_code, 200)
        response_content = str(response.content)
        self.assertIn('antwoord', response_content)
        self.assertIn(settings.STUF_BG_ONTVANGER['organisatie'], response_content)
        self.assertIn(settings.STUF_BG_ONTVANGER['applicatie'], response_content)
        self.assertIn(settings.STUF_BG_ONTVANGER['administratie'], response_content)
        self.assertIn(settings.STUF_BG_ONTVANGER['gebruiker'], response_content)
        self.assertIn(settings.STUF_BG_ZENDER['organisatie'], response_content)
        self.assertIn(settings.STUF_BG_ZENDER['applicatie'], response_content)
        self.assertIn(settings.STUF_BG_ZENDER['administratie'], response_content)
        self.assertIn(settings.STUF_BG_ZENDER['gebruiker'], response_content)

    def test_get_kinderen_van_aanvrager(self):
        test_bsn = 123456789

        response = self.client.get_kinderen_van_aanvrager(test_bsn)

        self.assertEqual(response.status_code, 200)
        response_content = str(response.content)
        self.assertIn('antwoord', response_content)
        self.assertIn(settings.STUF_BG_ONTVANGER['organisatie'], response_content)
        self.assertIn(settings.STUF_BG_ONTVANGER['applicatie'], response_content)
        self.assertIn(settings.STUF_BG_ONTVANGER['administratie'], response_content)
        self.assertIn(settings.STUF_BG_ONTVANGER['gebruiker'], response_content)
        self.assertIn(settings.STUF_BG_ZENDER['organisatie'], response_content)
        self.assertIn(settings.STUF_BG_ZENDER['applicatie'], response_content)
        self.assertIn(settings.STUF_BG_ZENDER['administratie'], response_content)
        self.assertIn(settings.STUF_BG_ZENDER['gebruiker'], response_content)

    def test_get_natuurlijk_persoon(self):
        test_bsn = 123456789

        response = self.client.get_natuurlijk_persoon(test_bsn)

        self.assertEqual(response.status_code, 200)
        response_content = str(response.content)
        self.assertIn('antwoord', response_content)
        self.assertIn(settings.STUF_BG_ONTVANGER['organisatie'], response_content)
        self.assertIn(settings.STUF_BG_ONTVANGER['applicatie'], response_content)
        self.assertIn(settings.STUF_BG_ONTVANGER['administratie'], response_content)
        self.assertIn(settings.STUF_BG_ONTVANGER['gebruiker'], response_content)
        self.assertIn(settings.STUF_BG_ZENDER['organisatie'], response_content)
        self.assertIn(settings.STUF_BG_ZENDER['applicatie'], response_content)
        self.assertIn(settings.STUF_BG_ZENDER['administratie'], response_content)
        self.assertIn(settings.STUF_BG_ZENDER['gebruiker'], response_content)

    def test_get_vestiging(self):
        test_bsn = 123456789

        response = self.client.get_vestiging(test_bsn)

        self.assertEqual(response.status_code, 200)
        response_content = str(response.content)
        self.assertIn('antwoord', response_content)
        self.assertIn(settings.STUF_BG_ONTVANGER['organisatie'], response_content)
        self.assertIn(settings.STUF_BG_ONTVANGER['applicatie'], response_content)
        self.assertIn(settings.STUF_BG_ONTVANGER['administratie'], response_content)
        self.assertIn(settings.STUF_BG_ONTVANGER['gebruiker'], response_content)
        self.assertIn(settings.STUF_BG_ZENDER['organisatie'], response_content)
        self.assertIn(settings.STUF_BG_ZENDER['applicatie'], response_content)
        self.assertIn(settings.STUF_BG_ZENDER['administratie'], response_content)
        self.assertIn(settings.STUF_BG_ZENDER['gebruiker'], response_content)
