from django.template import loader
from django.urls import NoReverseMatch, reverse
from django.utils.module_loading import import_string

import requests_mock
from freezegun import freeze_time
from mock import patch
from rest_framework.test import APITestCase

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
from openpersonen.api.views.generic_responses import (
    get_404_response,
    get_expand_400_response,
)
from openpersonen.contrib.stufbg.models import StufBGClient


@patch(
    "openpersonen.api.data_classes.ingeschreven_personen.backend",
    import_string("openpersonen.contrib.stufbg.backend.default"),
)
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
                loader.render_to_string("response/ResponseOneIngeschrevenPersoon.xml"),
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
                loader.render_to_string("response/ResponseTwoIngeschrevenPersoon.xml"),
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
                loader.render_to_string("response/ResponseOneIngeschrevenPersoon.xml"),
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
                loader.render_to_string("response/ResponseOneIngeschrevenPersoon.xml"),
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
                loader.render_to_string("response/ResponseBG.xml"),
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
        url = reverse(
            "ingeschrevenpersonen-detail",
            kwargs={"burgerservicenummer": 111111111},
        )

        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), get_404_response(url))


@override_settings(OPENPERSONEN_USE_LOCAL_DATABASE=True)
class TestExpandParameter(APITestCase):
    def setUp(self):
        super().setUp()
        self.bsn = 123456789
        self.kind_bsn = 234567891
        self.ouder_bsn = 345678912
        self.partnerschap_bsn = 456789123
        self.persoon = PersoonFactory.create(burgerservicenummer_persoon=self.bsn)
        self.kind = KindFactory(
            persoon=self.persoon, burgerservicenummer_kind=self.kind_bsn
        )
        self.ouder = OuderFactory(
            persoon=self.persoon, burgerservicenummer_ouder=self.ouder_bsn
        )
        self.partnerschap = PartnerschapFactory(
            persoon=self.persoon,
            burgerservicenummer_echtgenoot_geregistreerd_partner=self.partnerschap_bsn,
        )
        self.token = TokenFactory.create()

    def test_expand_parameter_not_included_relatives_not_included(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/expand.feature#L45
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list") + f"?burgerservicenummer={self.bsn}",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]
        self.assertEqual(
            data["_links"]["partners"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/partners",
        )
        self.assertEqual(
            data["_links"]["kinderen"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/kinderen",
        )
        self.assertEqual(
            data["_links"]["ouders"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/ouders",
        )
        self.assertNotIn("kinderen", data["_embedded"])
        self.assertNotIn("partners", data["_embedded"])
        self.assertNotIn("ouders", data["_embedded"])

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            ),
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(
            data["_links"]["partners"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/partners",
        )
        self.assertEqual(
            data["_links"]["kinderen"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/kinderen",
        )
        self.assertEqual(
            data["_links"]["ouders"]["href"],
            f"http://testserver.com/api/ingeschrevenpersonen/{self.bsn}/ouders",
        )
        self.assertNotIn("kinderen", data["_embedded"])
        self.assertNotIn("partners", data["_embedded"])
        self.assertNotIn("ouders", data["_embedded"])

    def test_expand_parameter_errors_when_not_allowed(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/expand.feature#L53
        """
        url = (
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=true"
        )
        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), get_expand_400_response(url, "true"))

        url = (
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + f"?expand=true"
        )
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), get_expand_400_response(url, "true"))

        url = (
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=True"
        )
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), get_expand_400_response(url, "True"))

        url = (
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + f"?expand=True"
        )
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), get_expand_400_response(url, "True"))

        url = (
            reverse("ingeschrevenpersonen-list")
            + f"?naam__geslachtsnaam={self.persoon.geslachtsnaam_persoon}&geboorte__datum={self.persoon.geboortedatum_persoon}&expand=true"
        )
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), get_expand_400_response(url, "true"))

    def test_expand_parameter_errors_with_incorrect_resource(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.1.0/features/expand.feature#L67
        """
        url = (
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=resourcebestaatniet"
        )
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), get_expand_400_response(url, "resourcebestaatniet")
        )

        url = (
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + f"?expand=resourcebestaatniet"
        )
        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), get_expand_400_response(url, "resourcebestaatniet")
        )

        url = (
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=reisdocumenten"
        )
        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), get_expand_400_response(url, "reisdocumenten")
        )

        url = (
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + f"?expand=reisdocumenten"
        )
        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), get_expand_400_response(url, "reisdocumenten")
        )

        url = (
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=ouders.veldbestaatniet"
        )
        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), get_expand_400_response(url, "veldbestaatniet")
        )

        url = (
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + f"?expand=ouders.veldbestaatniet"
        )
        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), get_expand_400_response(url, "veldbestaatniet")
        )

    def test_expand_parameter_errors_when_empty(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.1.0/features/expand.feature#L80
        """
        url = (
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand="
        )
        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), get_expand_400_response(url, ""))

        url = (
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + f"?expand="
        )
        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), get_expand_400_response(url, ""))

    def test_expand_parameter_with_multiple_resources(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.1.0/features/expand.feature#L85
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=partners,kinderen",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]["_embedded"]
        self.assertEqual(data["kinderen"][0]["burgerservicenummer"], str(self.kind_bsn))
        self.assertEqual(
            data["partners"][0]["burgerservicenummer"], str(self.partnerschap_bsn)
        )
        self.assertIsNone(data.get("ouders"))

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + f"?expand=partners,kinderen",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]
        self.assertEqual(data["kinderen"][0]["burgerservicenummer"], str(self.kind_bsn))
        self.assertEqual(
            data["partners"][0]["burgerservicenummer"], str(self.partnerschap_bsn)
        )
        self.assertIsNone(data.get("ouders"))

    def test_expand_parameter_with_dot_notation(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/expand.feature#L94
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=ouders.geslachtsaanduiding,ouders.burgerservicenummer",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]["_embedded"]
        self.assertEqual(
            self.ouder.geslachtsaanduiding_ouder, data["ouders"]["geslachtsaanduiding"]
        )
        self.assertEqual(
            str(self.ouder.burgerservicenummer_ouder),
            data["ouders"]["burgerservicenummer"],
        )

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + f"?expand=ouders.geslachtsaanduiding,ouders.burgerservicenummer",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]
        self.assertEqual(
            self.ouder.geslachtsaanduiding_ouder, data["ouders"]["geslachtsaanduiding"]
        )
        self.assertEqual(
            str(self.ouder.burgerservicenummer_ouder),
            data["ouders"]["burgerservicenummer"],
        )

    def test_expand_parameter_with_dot_notation_of_entire_data_group(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/expand.feature#L110
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=kinderen.naam,kinderen.geboorte",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]["_embedded"]
        self.assertEqual(
            data["kinderen"]["_embedded"]["naam"]["geslachtsnaam"],
            self.kind.geslachtsnaam_kind,
        )
        self.assertEqual(
            data["kinderen"]["_embedded"]["naam"]["voornamen"], self.kind.voornamen_kind
        )
        self.assertEqual(
            data["kinderen"]["_embedded"]["naam"]["voorvoegsel"],
            self.kind.voorvoegsel_geslachtsnaam_kind,
        )
        self.assertEqual(
            data["kinderen"]["_embedded"]["geboorte"]["_embedded"]["datum"]["datum"],
            str(self.kind.geboortedatum_kind),
        )
        self.assertEqual(
            data["kinderen"]["_embedded"]["geboorte"]["_embedded"]["land"][
                "omschrijving"
            ],
            str(self.kind.geboorteland_kind),
        )
        self.assertEqual(
            data["kinderen"]["_embedded"]["geboorte"]["_embedded"]["plaats"][
                "omschrijving"
            ],
            str(self.kind.geboorteplaats_kind),
        )
        self.assertIsNone(data["kinderen"]["_embedded"].get("burgerservicenummer"))
        self.assertIsNone(data.get("ouders"))
        self.assertIsNone(data.get("partners"))

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + f"?expand=kinderen.naam,kinderen.geboorte",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]
        self.assertEqual(
            data["kinderen"]["_embedded"]["naam"]["geslachtsnaam"],
            self.kind.geslachtsnaam_kind,
        )
        self.assertEqual(
            data["kinderen"]["_embedded"]["naam"]["voornamen"], self.kind.voornamen_kind
        )
        self.assertEqual(
            data["kinderen"]["_embedded"]["naam"]["voorvoegsel"],
            self.kind.voorvoegsel_geslachtsnaam_kind,
        )
        self.assertEqual(
            data["kinderen"]["_embedded"]["geboorte"]["_embedded"]["datum"]["datum"],
            str(self.kind.geboortedatum_kind),
        )
        self.assertEqual(
            data["kinderen"]["_embedded"]["geboorte"]["_embedded"]["land"][
                "omschrijving"
            ],
            str(self.kind.geboorteland_kind),
        )
        self.assertEqual(
            data["kinderen"]["_embedded"]["geboorte"]["_embedded"]["plaats"][
                "omschrijving"
            ],
            str(self.kind.geboorteplaats_kind),
        )
        self.assertIsNone(data["kinderen"]["_embedded"].get("burgerservicenummer"))
        self.assertIsNone(data.get("ouders"))
        self.assertIsNone(data.get("partners"))

    def test_expand_parameter_with_dot_notation_of_portion_of_data_group(self):
        """
        https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/expand.feature#L128
        """
        response = self.client.get(
            reverse("ingeschrevenpersonen-list")
            + f"?burgerservicenummer={self.bsn}&expand=kinderen.naam.voornamen,kinderen.naam.geslachtsnaam",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["ingeschrevenpersonen"][0]["_embedded"][
            "kinderen"
        ]["_embedded"]["naam"]
        self.assertEqual(len(data), 2)
        self.assertEqual(data["voornamen"], self.kind.voornamen_kind)
        self.assertEqual(data["geslachtsnaam"], self.kind.geslachtsnaam_kind)

        response = self.client.get(
            reverse(
                "ingeschrevenpersonen-detail", kwargs={"burgerservicenummer": self.bsn}
            )
            + "?expand=kinderen.naam.voornamen,kinderen.naam.geslachtsnaam",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()["_embedded"]["kinderen"]["_embedded"]["naam"]
        self.assertEqual(len(data), 2)
        self.assertEqual(data["voornamen"], self.kind.voornamen_kind)
        self.assertEqual(data["geslachtsnaam"], self.kind.geslachtsnaam_kind)
