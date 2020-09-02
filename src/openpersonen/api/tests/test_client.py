from django.template import loader
from django.test import TestCase

import requests_mock
from mock import patch

from openpersonen.api.client import Client
from openpersonen.config.models import StufBGConfig


class TestClient(TestCase):
    def setUp(self):
        self.client = Client()
        config = StufBGConfig.get_solo()
        self.url = config.url
        self.url = config.url
        self.zender_organisatie = config.zender_organisatie
        self.zender_applicatie = config.zender_applicatie
        self.zender_administratie = config.zender_administratie
        self.zender_gebruiker = config.zender_gebruiker
        self.ontvanger_organisatie = config.ontvanger_organisatie
        self.ontvanger_applicatie = config.ontvanger_applicatie
        self.ontvanger_administratie = config.ontvanger_administratie
        self.ontvanger_gebruiker = config.ontvanger_gebruiker

    @patch("django.utils.dateformat.format")
    @patch("uuid.uuid4")
    def test_get_ingeschreven_persoon(self, uuid_mock, dateformat_mock):
        test_bsn = 123456789
        test_uuid = "00000000-0000-0000-0000-000000000000"
        test_dateformat = "20200919094000"
        uuid_mock.return_value = test_uuid
        dateformat_mock.return_value = test_dateformat

        with requests_mock.Mocker() as m:
            m.post(
                self.url,
                content=bytes(
                    loader.render_to_string("ResponseIngeschrevenPersoon.xml"),
                    encoding="utf-8",
                ),
            )
            response = self.client.get_ingeschreven_persoon(test_bsn)
            self.assertTrue(m.called)

        self.assertEqual(response.status_code, 200)
        response_content = str(response.content)
        self.assertIn("antwoord", response_content)
        self.assertIn(self.zender_organisatie, response_content)
        self.assertIn(self.zender_applicatie, response_content)
        self.assertIn(self.zender_administratie, response_content)
        self.assertIn(self.zender_gebruiker, response_content)
        self.assertIn(self.ontvanger_organisatie, response_content)
        self.assertIn(self.ontvanger_applicatie, response_content)
        self.assertIn(self.ontvanger_administratie, response_content)
        self.assertIn(self.ontvanger_gebruiker, response_content)
        self.assertIn(test_uuid, response_content)
        self.assertIn(test_dateformat, response_content)

    @patch("django.utils.dateformat.format")
    @patch("uuid.uuid4")
    def test_get_kind(self, uuid_mock, dateformat_mock):
        test_bsn = 123456789
        test_uuid = "00000000-0000-0000-0000-000000000000"
        test_dateformat = "20200919094000"
        uuid_mock.return_value = test_uuid
        dateformat_mock.return_value = test_dateformat

        with requests_mock.Mocker() as m:
            m.post(
                self.url,
                content=bytes(
                    loader.render_to_string("ResponseKind.xml"), encoding="utf-8"
                ),
            )
            response = self.client.get_kind(test_bsn)
            self.assertTrue(m.called)

        self.assertEqual(response.status_code, 200)
        response_content = str(response.content)
        self.assertIn("antwoord", response_content)
        self.assertIn(self.zender_organisatie, response_content)
        self.assertIn(self.zender_applicatie, response_content)
        self.assertIn(self.zender_administratie, response_content)
        self.assertIn(self.zender_gebruiker, response_content)
        self.assertIn(self.ontvanger_organisatie, response_content)
        self.assertIn(self.ontvanger_applicatie, response_content)
        self.assertIn(self.ontvanger_administratie, response_content)
        self.assertIn(self.ontvanger_gebruiker, response_content)
        self.assertIn(test_uuid, response_content)
        self.assertIn(test_dateformat, response_content)

    @patch("django.utils.dateformat.format")
    @patch("uuid.uuid4")
    def test_get_ouder(self, uuid_mock, dateformat_mock):
        test_bsn = 123456789
        test_uuid = "00000000-0000-0000-0000-000000000000"
        test_dateformat = "20200919094000"
        uuid_mock.return_value = test_uuid
        dateformat_mock.return_value = test_dateformat

        with requests_mock.Mocker() as m:
            m.post(
                self.url,
                content=bytes(
                    loader.render_to_string("ResponseOuder.xml"), encoding="utf-8"
                ),
            )
            response = self.client.get_ouder(test_bsn)
            self.assertTrue(m.called)

        self.assertEqual(response.status_code, 200)
        response_content = str(response.content)
        self.assertIn("antwoord", response_content)
        self.assertIn(self.zender_organisatie, response_content)
        self.assertIn(self.zender_applicatie, response_content)
        self.assertIn(self.zender_administratie, response_content)
        self.assertIn(self.zender_gebruiker, response_content)
        self.assertIn(self.ontvanger_organisatie, response_content)
        self.assertIn(self.ontvanger_applicatie, response_content)
        self.assertIn(self.ontvanger_administratie, response_content)
        self.assertIn(self.ontvanger_gebruiker, response_content)
        self.assertIn(test_uuid, response_content)
        self.assertIn(test_dateformat, response_content)

    @patch("django.utils.dateformat.format")
    @patch("uuid.uuid4")
    def test_get_partner(self, uuid_mock, dateformat_mock):
        test_bsn = 123456789
        test_uuid = "00000000-0000-0000-0000-000000000000"
        test_dateformat = "20200919094000"
        uuid_mock.return_value = test_uuid
        dateformat_mock.return_value = test_dateformat

        with requests_mock.Mocker() as m:
            m.post(
                self.url,
                content=bytes(
                    loader.render_to_string("ResponsePartner.xml"), encoding="utf-8"
                ),
            )
            response = self.client.get_partner(test_bsn)
            self.assertTrue(m.called)

        self.assertEqual(response.status_code, 200)
        response_content = str(response.content)
        self.assertIn("antwoord", response_content)
        self.assertIn(self.zender_organisatie, response_content)
        self.assertIn(self.zender_applicatie, response_content)
        self.assertIn(self.zender_administratie, response_content)
        self.assertIn(self.zender_gebruiker, response_content)
        self.assertIn(self.ontvanger_organisatie, response_content)
        self.assertIn(self.ontvanger_applicatie, response_content)
        self.assertIn(self.ontvanger_administratie, response_content)
        self.assertIn(self.ontvanger_gebruiker, response_content)
        self.assertIn(test_uuid, response_content)
        self.assertIn(test_dateformat, response_content)
