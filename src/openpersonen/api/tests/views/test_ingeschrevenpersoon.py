from django.template import loader
from django.test import override_settings
from django.urls import NoReverseMatch, reverse

import requests_mock
from freezegun import freeze_time
from rest_framework.test import APITestCase

from openpersonen.api.models import StufBGClient
from openpersonen.api.tests.factory_models import (
    GezagsVerhoudingFactory,
    InschrijvingFactory,
    KiesrechtFactory,
    KindFactory,
    NationaliteitFactory,
    OuderFactory,
    OverlijdenFactory,
    PartnerschapFactory,
    PersoonFactory,
    ReisdocumentFactory,
    TokenFactory,
    VerblijfplaatsFactory,
    VerblijfstitelFactory,
)
from openpersonen.api.tests.test_data import INGESCHREVEN_PERSOON_RETRIEVE_DATA
from openpersonen.api.views import IngeschrevenPersoonViewSet
from openpersonen.api.views.generic_responses import RESPONSE_DATA_404


@override_settings(USE_STUF_BG_DATABASE=False)
class TestIngeschrevenPersoon(APITestCase):
    def setUp(self):
        super().setUp()
        self.url = StufBGClient.get_solo().url
        self.token = TokenFactory.create()
        self.bsn = 123456789

    def test_ingeschreven_persoon_without_token(self):
        response = self.client.get(reverse("ingeschrevenpersonen-list"))
        self.assertEqual(response.status_code, 401)

    def test_ingeschreven_persoon_with_no_proper_query_params(self):
        response = self.client.get(
            reverse("ingeschrevenpersonen-list"),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), "Exactly one combination of filters must be supplied"
        )

    def test_ingeschreven_persoon_without_proper_query_params(self):
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&naam__geslachtsnaam==Maykin",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), "Exactly one combination of filters must be supplied"
        )

    @requests_mock.Mocker()
    def test_ingeschreven_persoon_with_token_and_proper_query_params(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseOneIngeschrevenPersoon.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + f"?burgerservicenummer={self.bsn}",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)

    @requests_mock.Mocker()
    def test_list_ingeschreven_persoon(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseTwoIngeschrevenPersoon.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + "?verblijfplaats__identificatiecodenummeraanduiding=A",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        data = response.json()["_embedded"]["ingeschrevenpersonen"]
        self.assertEqual(len(data), 2)

    @requests_mock.Mocker()
    def test_list_ingeschreven_persoon_with_ingeschreven_persoon(self, post_mock):
        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseOneIngeschrevenPersoon.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + "?verblijfplaats__identificatiecodenummeraanduiding=A",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        data = response.json()["_embedded"]["ingeschrevenpersonen"]
        self.assertEqual(len(data), 1)

    @freeze_time("2020-09-12")
    @requests_mock.Mocker()
    def test_detail_ingeschreven_persoon(self, post_mock):

        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseOneIngeschrevenPersoon.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail",
                kwargs={"burgerservicenummer": self.bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), INGESCHREVEN_PERSOON_RETRIEVE_DATA)

    @freeze_time("2020-09-12")
    @requests_mock.Mocker()
    def test_detail_ingeschreven_persoon_BG_response(self, post_mock):
        fake_bsn = 123456780

        post_mock.post(
            self.url,
            content=bytes(
                loader.render_to_string("ResponseBG.xml"),
                encoding="utf-8",
            ),
        )

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail",
                kwargs={"burgerservicenummer": fake_bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json()["burgerservicenummer"], str(fake_bsn))

    def test_detail_ingeschreven_persoon_with_bad_burgerservicenummer(self):

        with self.assertRaises(NoReverseMatch):
            self.client.get(
                reverse(
                    "ingeschrevenpersonen-detail",
                    kwargs={"burgerservicenummer": "badbsn"},
                ),
                HTTP_AUTHORIZATION=f"Token {self.token.key}",
            )

    def test_get_filter_parameters(self):
        view = IngeschrevenPersoonViewSet()
        self.assertEqual(view.get_filter_parameters(), [])


@override_settings(USE_STUF_BG_DATABASE=True)
class TestIngeschrevenPersoonWithTestingModels(APITestCase):
    def setUp(self):
        super().setUp()
        self.bsn = 123456789
        self.persoon = PersoonFactory.create(burgerservicenummer_persoon=self.bsn)
        self.gezagsverhouding = GezagsVerhoudingFactory(persoon=self.persoon)
        self.inschrijving = InschrijvingFactory(persoon=self.persoon)
        self.kiesrecht = KiesrechtFactory(persoon=self.persoon)
        self.kind = KindFactory(persoon=self.persoon)
        self.nationaliteit = NationaliteitFactory(persoon=self.persoon)
        self.ouder = OuderFactory(persoon=self.persoon)
        self.overlijden = OverlijdenFactory(persoon=self.persoon)
        self.partnerschap = PartnerschapFactory(persoon=self.persoon)
        self.reisdocument = ReisdocumentFactory(persoon=self.persoon)
        self.verblijfplaats = VerblijfplaatsFactory(persoon=self.persoon)
        self.verblijfstitel = VerblijfstitelFactory(persoon=self.persoon)
        self.token = TokenFactory.create()

    def test_ingeschreven_persoon_without_token(self):
        response = self.client.get(reverse("ingeschrevenpersonen-list"))
        self.assertEqual(response.status_code, 401)

    def test_ingeschreven_persoon_with_token_and_proper_query_params(self):

        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + f"?burgerservicenummer={self.bsn}",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]
        self.assertEqual(data["burgerservicenummer"], str(self.bsn))
        self.assertEqual(
            data["_embedded"]["naam"]["geslachtsnaam"],
            self.persoon.geslachtsnaam_persoon,
        )
        self.assertEqual(
            data["_embedded"]["naam"]["_embedded"]["inOnderzoek"]["_embedded"][
                "datumIngangOnderzoek"
            ]["datum"],
            str(self.persoon.datum_ingang_onderzoek),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["datum"]["datum"],
            str(self.persoon.geboortedatum_persoon),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["land"]["omschrijving"],
            str(self.persoon.geboorteland_persoon),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["plaats"]["omschrijving"],
            str(self.persoon.geboorteplaats_persoon),
        )
        self.assertEqual(
            data["_embedded"]["kiesrecht"]["_embedded"][
                "einddatumUitsluitingEuropeesKiesrecht"
            ]["datum"],
            str(self.kiesrecht.einddatum_uitsluiting_europees_kiesrecht),
        )
        self.assertEqual(
            data["_embedded"]["kiesrecht"]["_embedded"][
                "einddatumUitsluitingKiesrecht"
            ]["datum"],
            str(self.kiesrecht.einddatum_uitsluiting_kiesrecht),
        )
        self.assertEqual(
            data["_embedded"]["nationaliteit"][0]["_embedded"]["datumIngangGeldigheid"][
                "datum"
            ],
            str(self.nationaliteit.datum_van_ingang_geldigheid_met_betrekking),
        )
        self.assertEqual(
            data["_embedded"]["nationaliteit"][0]["_embedded"]["nationaliteit"][
                "omschrijving"
            ],
            str(self.nationaliteit.nationaliteit),
        )
        self.assertEqual(
            data["_embedded"]["nationaliteit"][0]["_embedded"]["redenOpname"][
                "omschrijving"
            ],
            str(self.nationaliteit.reden_opname_nationaliteit),
        )
        self.assertEqual(
            data["_embedded"]["nationaliteit"][0]["_embedded"]["inOnderzoek"][
                "_embedded"
            ]["datumIngangOnderzoek"]["datum"],
            str(self.nationaliteit.datum_ingang_onderzoek),
        )
        self.assertEqual(
            data["_embedded"]["overlijden"]["_embedded"]["datum"]["datum"],
            str(self.overlijden.datum_overlijden),
        )
        self.assertEqual(
            data["_embedded"]["overlijden"]["_embedded"]["land"]["omschrijving"],
            str(self.overlijden.land_overlijden),
        )
        self.assertEqual(
            data["_embedded"]["overlijden"]["_embedded"]["plaats"]["omschrijving"],
            str(self.overlijden.plaats_overlijden),
        )
        self.assertEqual(
            data["_embedded"]["verblijfplaats"]["identificatiecodeNummeraanduiding"],
            self.verblijfplaats.identificatiecode_nummeraanduiding,
        )
        self.assertEqual(
            data["_embedded"]["gezagsverhouding"]["_embedded"]["inOnderzoek"][
                "_embedded"
            ]["datumIngangOnderzoek"]["datum"],
            str(self.gezagsverhouding.datum_ingang_onderzoek),
        )
        self.assertEqual(
            data["_embedded"]["reisdocumenten"][0],
            self.reisdocument.nummer_nederlands_reisdocument,
        )
        self.assertEqual(
            data["_embedded"]["verblijfstitel"]["_embedded"]["aanduiding"][
                "omschrijving"
            ],
            str(self.verblijfstitel.aanduiding_verblijfstitel),
        )
        self.assertEqual(
            data["_embedded"]["verblijfstitel"]["_embedded"]["datumEinde"]["datum"],
            str(self.verblijfstitel.datum_einde_verblijfstitel),
        )
        self.assertEqual(
            data["_embedded"]["verblijfstitel"]["_embedded"]["datumIngang"]["datum"],
            str(self.verblijfstitel.ingangsdatum_verblijfstitel),
        )
        self.assertEqual(
            data["_embedded"]["verblijfstitel"]["_embedded"]["inOnderzoek"][
                "_embedded"
            ]["datumIngangOnderzoek"]["datum"],
            str(self.verblijfstitel.datum_ingang_onderzoek),
        )

    def test_ingeschreven_persoon_with_token_and_incorrect_proper_query_params(self):

        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + "?burgerservicenummer=1",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["_embedded"]["ingeschrevenpersonen"], [])

    def test_detail_ingeschreven_persoon(self):

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail",
                kwargs={"burgerservicenummer": self.bsn},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["burgerservicenummer"], str(self.bsn))
        self.assertEqual(
            data["_embedded"]["naam"]["geslachtsnaam"],
            self.persoon.geslachtsnaam_persoon,
        )
        self.assertEqual(
            data["_embedded"]["naam"]["_embedded"]["inOnderzoek"]["_embedded"][
                "datumIngangOnderzoek"
            ]["datum"],
            str(self.persoon.datum_ingang_onderzoek),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["datum"]["datum"],
            str(self.persoon.geboortedatum_persoon),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["land"]["omschrijving"],
            str(self.persoon.geboorteland_persoon),
        )
        self.assertEqual(
            data["_embedded"]["geboorte"]["_embedded"]["plaats"]["omschrijving"],
            str(self.persoon.geboorteplaats_persoon),
        )
        self.assertEqual(
            data["_embedded"]["kiesrecht"]["_embedded"][
                "einddatumUitsluitingEuropeesKiesrecht"
            ]["datum"],
            str(self.kiesrecht.einddatum_uitsluiting_europees_kiesrecht),
        )
        self.assertEqual(
            data["_embedded"]["kiesrecht"]["_embedded"][
                "einddatumUitsluitingKiesrecht"
            ]["datum"],
            str(self.kiesrecht.einddatum_uitsluiting_kiesrecht),
        )
        self.assertEqual(
            data["_embedded"]["nationaliteit"][0]["_embedded"]["datumIngangGeldigheid"][
                "datum"
            ],
            str(self.nationaliteit.datum_van_ingang_geldigheid_met_betrekking),
        )
        self.assertEqual(
            data["_embedded"]["nationaliteit"][0]["_embedded"]["nationaliteit"][
                "omschrijving"
            ],
            str(self.nationaliteit.nationaliteit),
        )
        self.assertEqual(
            data["_embedded"]["nationaliteit"][0]["_embedded"]["redenOpname"][
                "omschrijving"
            ],
            str(self.nationaliteit.reden_opname_nationaliteit),
        )
        self.assertEqual(
            data["_embedded"]["nationaliteit"][0]["_embedded"]["inOnderzoek"][
                "_embedded"
            ]["datumIngangOnderzoek"]["datum"],
            str(self.nationaliteit.datum_ingang_onderzoek),
        )
        self.assertEqual(
            data["_embedded"]["overlijden"]["_embedded"]["datum"]["datum"],
            str(self.overlijden.datum_overlijden),
        )
        self.assertEqual(
            data["_embedded"]["overlijden"]["_embedded"]["land"]["omschrijving"],
            str(self.overlijden.land_overlijden),
        )
        self.assertEqual(
            data["_embedded"]["overlijden"]["_embedded"]["plaats"]["omschrijving"],
            str(self.overlijden.plaats_overlijden),
        )
        self.assertEqual(
            data["_embedded"]["verblijfplaats"]["identificatiecodeNummeraanduiding"],
            self.verblijfplaats.identificatiecode_nummeraanduiding,
        )
        self.assertEqual(
            data["_embedded"]["gezagsverhouding"]["_embedded"]["inOnderzoek"][
                "_embedded"
            ]["datumIngangOnderzoek"]["datum"],
            str(self.gezagsverhouding.datum_ingang_onderzoek),
        )
        self.assertEqual(
            data["_embedded"]["reisdocumenten"][0],
            self.reisdocument.nummer_nederlands_reisdocument,
        )
        self.assertEqual(
            data["_embedded"]["verblijfstitel"]["_embedded"]["aanduiding"][
                "omschrijving"
            ],
            str(self.verblijfstitel.aanduiding_verblijfstitel),
        )
        self.assertEqual(
            data["_embedded"]["verblijfstitel"]["_embedded"]["datumEinde"]["datum"],
            str(self.verblijfstitel.datum_einde_verblijfstitel),
        )
        self.assertEqual(
            data["_embedded"]["verblijfstitel"]["_embedded"]["datumIngang"]["datum"],
            str(self.verblijfstitel.ingangsdatum_verblijfstitel),
        )
        self.assertEqual(
            data["_embedded"]["verblijfstitel"]["_embedded"]["inOnderzoek"][
                "_embedded"
            ]["datumIngangOnderzoek"]["datum"],
            str(self.verblijfstitel.datum_ingang_onderzoek),
        )

    def test_not_found_detail_ingeschreven_persoon(self):

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail",
                kwargs={"burgerservicenummer": 111111111},
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), RESPONSE_DATA_404)
