from mock import patch

from django.conf import settings
from django.test import TestCase

from openpersonen.api.client import Client


class TestClient(TestCase):

    def setUp(self):
        self.client = Client()

    @patch('django.utils.dateformat.format')
    @patch('uuid.uuid4')
    def test_get_gezinssituatie_op_adres_aanvrager(self, uuid_mock, dateformat_mock):
        test_bsn = 123456789
        test_uuid = '00000000-0000-0000-0000-000000000000'
        test_dateformat = '20200919094000'
        uuid_mock.return_value = test_uuid
        dateformat_mock.return_value = test_dateformat

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
        self.assertIn(test_uuid, response_content)
        self.assertIn(test_dateformat, response_content)
        # Assert contents at proper places
        self.assertTrue(response_content.find('<StUF:zender>') <
                        response_content.find('Open Personen') <
                        response_content.find('</StUF:zender>'))
        self.assertTrue(response_content.find('<StUF:ontvanger>') <
                        response_content.find('BG-mock') <
                        response_content.find('</StUF:ontvanger>'))

    @patch('django.utils.dateformat.format')
    @patch('uuid.uuid4')
    def test_get_kinderen_van_aanvrager(self, uuid_mock, dateformat_mock):
        test_bsn = 123456789
        test_uuid = '00000000-0000-0000-0000-000000000000'
        test_dateformat = '20200919094000'
        uuid_mock.return_value = test_uuid
        dateformat_mock.return_value = test_dateformat

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
        self.assertIn(test_uuid, response_content)
        self.assertIn(test_dateformat, response_content)
        # Assert contents at proper places
        self.assertTrue(response_content.find('<StUF:zender>') <
                        response_content.find('Open Personen') <
                        response_content.find('</StUF:zender>'))
        self.assertTrue(response_content.find('<StUF:ontvanger>') <
                        response_content.find('BG-mock') <
                        response_content.find('</StUF:ontvanger>'))

    @patch('django.utils.dateformat.format')
    @patch('uuid.uuid4')
    def test_get_natuurlijk_persoon(self, uuid_mock, dateformat_mock):
        test_bsn = 123456789
        test_uuid = '00000000-0000-0000-0000-000000000000'
        test_dateformat = '20200919094000'
        uuid_mock.return_value = test_uuid
        dateformat_mock.return_value = test_dateformat

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
        self.assertIn(test_uuid, response_content)
        self.assertIn(test_dateformat, response_content)
        # Assert contents at proper places
        self.assertTrue(response_content.find('<StUF:zender>') <
                        response_content.find('Open Personen') <
                        response_content.find('</StUF:zender>'))
        self.assertTrue(response_content.find('<StUF:ontvanger>') <
                        response_content.find('BG-mock') <
                        response_content.find('</StUF:ontvanger>'))

    @patch('django.utils.dateformat.format')
    @patch('uuid.uuid4')
    def test_get_vestiging(self, uuid_mock, dateformat_mock):
        test_bsn = 123456789
        test_uuid = '00000000-0000-0000-0000-000000000000'
        test_dateformat = '20200919094000'
        uuid_mock.return_value = test_uuid
        dateformat_mock.return_value = test_dateformat

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
        self.assertIn(test_uuid, response_content)
        self.assertIn(test_dateformat, response_content)
        # Assert contents at proper places
        self.assertTrue(response_content.find('<StUF:zender>') <
                        response_content.find('Open Personen') <
                        response_content.find('</StUF:zender>'))
        self.assertTrue(response_content.find('<StUF:ontvanger>') <
                        response_content.find('BG-mock') <
                        response_content.find('</StUF:ontvanger>'))
