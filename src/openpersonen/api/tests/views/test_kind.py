from django.template import loader
from django.test import override_settings
from django.urls import NoReverseMatch, reverse

import requests_mock
from freezegun import freeze_time
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from openpersonen.accounts.models import User
from openpersonen.api.models import StufBGClient
from openpersonen.api.tests.factory_models import KindFactory, PersoonFactory
from openpersonen.api.tests.test_data import KIND_RETRIEVE_DATA
from openpersonen.api.views.generic_responses import RESPONSE_DATA_404


@override_settings(USE_STUF_BG_DATABASE=False)
class TestKind(APITestCase):
    def setUp(self):
        super().setUp()
        self.persoon_bsn = 123456789
        self.url = StufBGClient.get_solo().url
        self.user = User.objects.create(username="test")
        self.token = Token.objects.create(user=self.user)

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
                loader.render_to_string("ResponseTwoKinderen.xml"), encoding="utf-8"
            ),
        )

        response = self.client.get(
            reverse(
                "kinderen-list",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        data = response.json()['_embedded']['kinderen']
        self.assertEqual(len(data), 2)
        first_bsn = data[0]['burgerservicenummer']
        second_bsn = data[1]['burgerservicenummer']
        self.assertTrue(first_bsn == '789123456' or first_bsn == '456789123')
        self.assertTrue(second_bsn == '789123456' or second_bsn == '456789123')

    @requests_mock.Mocker()
    def test_list_kind_with_one_kind(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseOneKind.xml"), encoding="utf-8"
            ),
        )

        response = self.client.get(
            reverse(
                "kinderen-list",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        data = response.json()['_embedded']['kinderen']
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['burgerservicenummer'], '456789123')

    @freeze_time("2020-09-12")
    @requests_mock.Mocker()
    def test_detail_kind(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseOneKind.xml"), encoding="utf-8"
            ),
        )

        response = self.client.get(
            reverse(
                "kinderen-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": 456789123,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), KIND_RETRIEVE_DATA)

    @requests_mock.Mocker()
    def test_detail_kind_when_id_does_not_match(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseOneKind.xml"), encoding="utf-8"
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

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), dict())

    @requests_mock.Mocker()
    def test_detail_kind_with_two_kinderen(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseTwoKinderen.xml"), encoding="utf-8"
            ),
        )

        response = self.client.get(
            reverse(
                "kinderen-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": 456789123,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), KIND_RETRIEVE_DATA)

    @requests_mock.Mocker()
    def test_detail_kind_when_id_does_not_match_with_two_kinderen(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseTwoKinderen.xml"), encoding="utf-8"
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

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), dict())

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


@override_settings(USE_STUF_BG_DATABASE=True)
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

    def test_kind_without_token(self):
        response = self.client.get(
            reverse(
                "kinderen-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            )
        )
        self.assertEqual(response.status_code, 401)

    def test_kind_with_token(self):
        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "kinderen-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )
        self.assertEqual(response.status_code, 200)

    def test_list_kind(self):

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "kinderen-list",
                kwargs={"ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
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

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "kinderen-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": self.kind_bsn,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
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

        user = User.objects.create(username="test")
        token = Token.objects.create(user=user)
        response = self.client.get(
            reverse(
                "kinderen-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": self.persoon_bsn,
                    "id": 222222222,
                },
            ),
            HTTP_AUTHORIZATION=f"Token {token.key}",
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), RESPONSE_DATA_404)
