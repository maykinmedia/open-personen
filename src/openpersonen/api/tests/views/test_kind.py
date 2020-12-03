from django.template import loader
from django.urls import NoReverseMatch, reverse
from django.utils.module_loading import import_string

import requests_mock
from freezegun import freeze_time
from mock import patch
from rest_framework.test import APITestCase

from openpersonen.api.tests.factory_models import (
    KindFactory,
    PersoonFactory,
    TokenFactory,
)
from openpersonen.api.tests.test_data import KIND_RETRIEVE_DATA
from openpersonen.api.views.generic_responses import get_404_response
from openpersonen.contrib.stufbg.models import StufBGClient
from openpersonen.features.country_code.factory_models import CountryCodeFactory


@patch(
    "openpersonen.api.data_classes.persoon.backend",
    import_string("openpersonen.contrib.stufbg.backend.default"),
)
class TestKind(APITestCase):
    def setUp(self):
        super().setUp()
        self.persoon_bsn = 123456789
        self.kind_bsn = 456789123
        self.url = StufBGClient.get_solo().url
        self.token = TokenFactory.create()
        CountryCodeFactory.create()

    def test_kind_without_token(self):
        response = self.client.get(
            reverse(
                "kinderen-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            )
        )
        self.assertEqual(response.status_code, 401)

    @requests_mock.Mocker()
    def test_list_kind(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseTwoKinderen.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "kinderen-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        data = response.json()["_embedded"]["kinderen"]
        self.assertEqual(len(data), 2)
        first_bsn = data[0]["burgerservicenummer"]
        second_bsn = data[1]["burgerservicenummer"]
        self.assertTrue(first_bsn == "789123456" or first_bsn == str(self.kind_bsn))
        self.assertTrue(second_bsn == "789123456" or second_bsn == str(self.kind_bsn))

    @requests_mock.Mocker()
    def test_list_kind_with_one_kind(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseOneKind.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "kinderen-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        data = response.json()["_embedded"]["kinderen"]
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["burgerservicenummer"], str(self.kind_bsn))

    @freeze_time("2020-09-12")
    @requests_mock.Mocker()
    def test_detail_kind(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseOneKind.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "kinderen-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": self.kind_bsn,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), KIND_RETRIEVE_DATA)

    @requests_mock.Mocker()
    def test_detail_kind_BG_response(self, post_mock):
        fake_bsn = 123456780
        fake_kind_bsn = 123456781

        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseBG.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "kinderen-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": fake_bsn,
                    "id": fake_kind_bsn,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json()["burgerservicenummer"], str(fake_kind_bsn))

    @requests_mock.Mocker()
    def test_detail_kind_when_id_does_not_match(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseOneKind.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "kinderen-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": 111111111,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 404)
        self.assertTrue(post_mock.called)

    @requests_mock.Mocker()
    def test_detail_kind_with_two_kinderen(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseTwoKinderen.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "kinderen-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": self.kind_bsn,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.maxDiff = None
        self.assertEqual(response.json(), KIND_RETRIEVE_DATA)

    @requests_mock.Mocker()
    def test_detail_kind_when_id_does_not_match_with_two_kinderen(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("response/ResponseTwoKinderen.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "kinderen-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": 111111111,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 404)
        self.assertTrue(post_mock.called)

    def test_detail_kind_with_bad_id(self):

        with self.assertRaises(NoReverseMatch):
            self.client.get(
                reverse(
                    "kinderen-detail",
                    kwargs={
                        "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                        "id": "badid",
                    },
                ),
                HTTP_AUTHORIZATION=f"Token {self.token.key}",
            )


class TestKindWithTestingModels(APITestCase):
    def setUp(self):
        super().setUp()
        self.persoon_bsn = 123456789
        self.kind_bsn = 111111111
        self.persoon = PersoonFactory.create(
            burgerservicenummer_persoon=self.persoon_bsn
        )
        self.kind = KindFactory(
            persoon=self.persoon, burgerservicenummer_kind=self.kind_bsn
        )
        self.token = TokenFactory.create()

    def test_kind_without_token(self):
        response = self.client.get(
            reverse(
                "kinderen-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            )
        )
        self.assertEqual(response.status_code, 401)

    def test_kind_with_token(self):
        response = self.client.get(
            reverse(
                "kinderen-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)

    def test_list_kind(self):

        response = self.client.get(
            reverse(
                "kinderen-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json()["_embedded"]["kinderen"], list))
        data = response.json()["_embedded"]["kinderen"][0]
        self.assertEqual(
            data["burgerservicenummer"],
            str(self.kind_bsn),
        )
        self.assertEqual(
            data["_embedded"]["naam"]["voornamen"], self.kind.voornamen_kind
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["datum"]["datum"],
            str(self.kind.geboortedatum_kind),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["land"]["omschrijving"],
            str(self.kind.geboorteland_kind),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["plaats"]["omschrijving"],
            str(self.kind.geboorteplaats_kind),
        )
        self.assertEqual(
            data["_embedded"]["inOnderzoek"]["_embedded"]["datumIngangOnderzoek"][
                "datum"
            ],
            str(self.kind.datum_ingang_onderzoek),
        )

    def test_detail_kind(self):

        response = self.client.get(
            reverse(
                "kinderen-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": self.kind_bsn,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(
            data["burgerservicenummer"],
            str(self.kind_bsn),
        )
        self.assertEqual(
            data["_embedded"]["naam"]["voornamen"], self.kind.voornamen_kind
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["datum"]["datum"],
            str(self.kind.geboortedatum_kind),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["land"]["omschrijving"],
            str(self.kind.geboorteland_kind),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["plaats"]["omschrijving"],
            str(self.kind.geboorteplaats_kind),
        )
        self.assertEqual(
            data["_embedded"]["inOnderzoek"]["_embedded"]["datumIngangOnderzoek"][
                "datum"
            ],
            str(self.kind.datum_ingang_onderzoek),
        )

    def test_detail_kind_404(self):
        url = reverse(
            "kinderen-detail",
            kwargs={
                "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                "id": 222222222,
            },
        )

        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), get_404_response(url))
