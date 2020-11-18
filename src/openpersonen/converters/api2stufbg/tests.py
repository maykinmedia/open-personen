from django.urls import reverse

from freezegun import freeze_time
from mock import patch
from rest_framework.test import APITestCase

from openpersonen.contrib.stufbg.models import StufBGClient


class TestPersoonView(APITestCase):
    @freeze_time("2020-11-17")
    @patch("uuid.uuid4")
    def test_persoon_view(self, uuid_mock):
        uuid_mock.return_value = "00000000-0000-0000-0000-000000000000"
        bsn = 123456789
        expected_data = StufBGClient.get_solo().get_persoon_request_data(
            filters={"burgerservicenummer": str(bsn)}
        )

        response = self.client.get(
            reverse("api2stufbg:ingeschrevenpersonen-list")
            + f"?burgerservicenummer={bsn}"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)

    @freeze_time("2020-11-17")
    @patch("uuid.uuid4")
    def test_specific_persoon_view(self, uuid_mock):
        uuid_mock.return_value = "00000000-0000-0000-0000-000000000000"
        bsn = 123456789
        expected_data = StufBGClient.get_solo().get_persoon_request_data(bsn=bsn)

        response = self.client.get(
            reverse(
                "api2stufbg:ingeschrevenpersonen-detail",
                kwargs={"burgerservicenummer": bsn},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)


class TestOuderView(APITestCase):
    @freeze_time("2020-11-17")
    @patch("uuid.uuid4")
    def test_ouder_view(self, uuid_mock):
        uuid_mock.return_value = "00000000-0000-0000-0000-000000000000"
        bsn = 123456789
        expected_data = StufBGClient.get_solo().get_nested_request_data(
            "request/RequestOuder.xml", bsn
        )
        response = self.client.get(
            reverse(
                "api2stufbg:ouders-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": bsn},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)


class TestKindView(APITestCase):
    @freeze_time("2020-11-17")
    @patch("uuid.uuid4")
    def test_kind_view(self, uuid_mock):
        uuid_mock.return_value = "00000000-0000-0000-0000-000000000000"
        bsn = 123456789
        expected_data = StufBGClient.get_solo().get_nested_request_data(
            "request/RequestKind.xml", bsn
        )
        response = self.client.get(
            reverse(
                "api2stufbg:kinderen-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": bsn},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)


class TestPartnerView(APITestCase):
    @freeze_time("2020-11-17")
    @patch("uuid.uuid4")
    def test_partner_view(self, uuid_mock):
        uuid_mock.return_value = "00000000-0000-0000-0000-000000000000"
        bsn = 123456789
        expected_data = StufBGClient.get_solo().get_nested_request_data(
            "request/RequestPartner.xml", bsn
        )
        response = self.client.get(
            reverse(
                "api2stufbg:partners-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": bsn},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)
