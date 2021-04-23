import os

from django.template import loader
from django.test import TestCase
from django.test.testcases import LiveServerTestCase

import requests
import requests_mock
from mock import patch

from openpersonen.contrib.stufbg.models import StufBGClient


class TestClient(TestCase):
    def setUp(self):
        super().setUp()
        self.client = StufBGClient.get_solo()
        self.url = self.client.url
        self.zender_organisatie = self.client.zender_organisatie
        self.zender_applicatie = self.client.zender_applicatie
        self.zender_administratie = self.client.zender_administratie
        self.zender_gebruiker = self.client.zender_gebruiker
        self.ontvanger_organisatie = self.client.ontvanger_organisatie
        self.ontvanger_applicatie = self.client.ontvanger_applicatie
        self.ontvanger_administratie = self.client.ontvanger_administratie
        self.ontvanger_gebruiker = self.client.ontvanger_gebruiker

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
                    loader.render_to_string(
                        "response/ResponseOneIngeschrevenPersoon.xml",
                        context={
                            "referentienummer": test_uuid,
                            "tijdstip_bericht": test_dateformat,
                        },
                    ),
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
    def test_making_request_without_certificates(self, uuid_mock, dateformat_mock):
        self.client.certificate = None
        self.client.certificate_key = None
        self.client.save()
        test_bsn = 123456789
        test_uuid = "00000000-0000-0000-0000-000000000000"
        test_dateformat = "20200919094000"
        uuid_mock.return_value = test_uuid
        dateformat_mock.return_value = test_dateformat

        with requests_mock.Mocker() as m:
            m.post(
                self.url,
                content=bytes(
                    loader.render_to_string(
                        "response/ResponseOneIngeschrevenPersoon.xml",
                        context={
                            "referentienummer": test_uuid,
                            "tijdstip_bericht": test_dateformat,
                        },
                    ),
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
                    loader.render_to_string(
                        "response/ResponseOneKind.xml",
                        context={
                            "referentienummer": test_uuid,
                            "tijdstip_bericht": test_dateformat,
                        },
                    ),
                    encoding="utf-8",
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
                    loader.render_to_string(
                        "response/ResponseOneOuder.xml",
                        context={
                            "referentienummer": test_uuid,
                            "tijdstip_bericht": test_dateformat,
                        },
                    ),
                    encoding="utf-8",
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
                    loader.render_to_string(
                        "response/ResponseOnePartner.xml",
                        context={
                            "referentienummer": test_uuid,
                            "tijdstip_bericht": test_dateformat,
                        },
                    ),
                    encoding="utf-8",
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

    @patch("django.utils.dateformat.format")
    @patch("uuid.uuid4")
    def test_get_verblijf_plaats_historie(self, uuid_mock, dateformat_mock):
        test_bsn = 123456789
        test_uuid = "00000000-0000-0000-0000-000000000000"
        test_dateformat = "20200919094000"
        uuid_mock.return_value = test_uuid
        dateformat_mock.return_value = test_dateformat

        with requests_mock.Mocker() as m:
            m.post(
                self.url,
                content=bytes(
                    loader.render_to_string(
                        "response/ResponseVerblijfPlaatsHistorie.xml",
                        context={
                            "referentienummer": test_uuid,
                            "tijdstip_bericht": test_dateformat,
                        },
                    ),
                    encoding="utf-8",
                ),
            )
            response = self.client.get_verblijf_plaats_historie(test_bsn, {})
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
    def test_get_verblijfs_titel_historie(self, uuid_mock, dateformat_mock):
        test_bsn = 123456789
        test_uuid = "00000000-0000-0000-0000-000000000000"
        test_dateformat = "20200919094000"
        uuid_mock.return_value = test_uuid
        dateformat_mock.return_value = test_dateformat

        with requests_mock.Mocker() as m:
            m.post(
                self.url,
                content=bytes(
                    loader.render_to_string(
                        "response/ResponseVerblijfsTitelHistorie.xml",
                        context={
                            "referentienummer": test_uuid,
                            "tijdstip_bericht": test_dateformat,
                        },
                    ),
                    encoding="utf-8",
                ),
            )
            response = self.client.get_verblijfs_titel_historie(test_bsn, {})
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
    def test_get_partner_historie(self, uuid_mock, dateformat_mock):
        test_bsn = 123456789
        test_uuid = "00000000-0000-0000-0000-000000000000"
        test_dateformat = "20200919094000"
        uuid_mock.return_value = test_uuid
        dateformat_mock.return_value = test_dateformat

        with requests_mock.Mocker() as m:
            m.post(
                self.url,
                content=bytes(
                    loader.render_to_string(
                        "response/ResponsePartnerHistorie.xml",
                        context={
                            "referentienummer": test_uuid,
                            "tijdstip_bericht": test_dateformat,
                        },
                    ),
                    encoding="utf-8",
                ),
            )
            response = self.client.get_partner_historie(test_bsn, {})
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
    def test_get_nationaliteit_historie(self, uuid_mock, dateformat_mock):
        test_bsn = 123456789
        test_uuid = "00000000-0000-0000-0000-000000000000"
        test_dateformat = "20200919094000"
        uuid_mock.return_value = test_uuid
        dateformat_mock.return_value = test_dateformat

        with requests_mock.Mocker() as m:
            m.post(
                self.url,
                content=bytes(
                    loader.render_to_string(
                        "response/ResponseNationaliteitHistorie.xml",
                        context={
                            "referentienummer": test_uuid,
                            "tijdstip_bericht": test_dateformat,
                        },
                    ),
                    encoding="utf-8",
                ),
            )
            response = self.client.get_nationaliteit_historie(test_bsn, {})
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


class TestClientMakeRequest(LiveServerTestCase):
    def test_making_request_with_cert(self):
        ssl_crt = os.path.join(os.path.dirname(__file__), "certs", "mocks.crt")
        ssl_key = os.path.join(os.path.dirname(__file__), "certs", "mocks.key")
        response = requests.post(
            self.live_server_url, data={"foo": "bar"}, cert=(ssl_crt, ssl_key)
        )
        self.assertEqual(response.status_code, 403)

    def test_making_request_without_cert(self):
        ssl_crt = None
        ssl_key = None
        response = requests.post(
            self.live_server_url, data={"foo": "bar"}, cert=(ssl_crt, ssl_key)
        )
        self.assertEqual(response.status_code, 403)
