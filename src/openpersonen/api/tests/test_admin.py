from django.http import HttpRequest
from django.urls import reverse

from rest_framework.test import APITestCase

from openpersonen.api.demo_models import Kind, Ouder, Persoon
from openpersonen.api.tests.factory_models import PersoonFactory, UserFactory


class TestPersoonAdmin(APITestCase):
    def setUp(self):
        self.persoon = PersoonFactory.create(
            burgerservicenummer_persoon=123456789,
            voornamen_persoon="persoon_voornamen",
            geslachtsnaam_persoon="geslachtsnaam_persoon",
            geboortedatum_persoon="20200929",
            geslachtsaanduiding="M",
        )
        self.url = reverse(
            "admin:api_persoon_change", kwargs={"object_id": self.persoon.pk}
        )
        self.user = UserFactory(is_staff=True, is_superuser=True)
        self.client.login(
            request=HttpRequest(), username=self.user.username, password="secret"
        )

    def test_adding_kind(self):

        kind_burgerservicenummer = 987654321
        kind_voornamen = "kind_voornamen"
        kind_geslachtsnaam = "kind_geslachtsnaam"
        kind_geboortedatum = 20201031

        test_data = {
            "burgerservicenummer_persoon": self.persoon.burgerservicenummer_persoon,
            "voornamen_persoon": self.persoon.voornamen_persoon,
            "geslachtsnaam_persoon": self.persoon.geslachtsnaam_persoon,
            "geboortedatum_persoon": self.persoon.geboortedatum_persoon,
            "geslachtsaanduiding": self.persoon.geslachtsaanduiding,
            "kind_set-TOTAL_FORMS": "1",
            "kind_set-INITIAL_FORMS": "0",
            "kind_set-MIN_NUM_FORMS": "0",
            "kind_set-MAX_NUM_FORMS": "1000",
            "kind_set-0-id": "",
            "kind_set-0-persoon": self.persoon.id,
            "kind_set-0-burgerservicenummer_kind": kind_burgerservicenummer,
            "kind_set-0-voornamen_kind": kind_voornamen,
            "kind_set-0-geslachtsnaam_kind": kind_geslachtsnaam,
            "kind_set-0-geboortedatum_kind": kind_geboortedatum,
            "kind_set-__prefix__-id": "",
            "kind_set-__prefix__-persoon": self.persoon.id,
            "kind_set-__prefix__-burgerservicenummer_kind": "",
            "kind_set-__prefix__-voornamen_kind": "",
            "kind_set-__prefix__-geslachtsnaam_kind": "",
            "kind_set-__prefix__-geboortedatum_kind": "",
            "ouder_set-TOTAL_FORMS": "0",
            "ouder_set-INITIAL_FORMS": "0",
            "ouder_set-MIN_NUM_FORMS": "0",
            "ouder_set-MAX_NUM_FORMS": "1000",
            "ouder_set-__prefix__-id": "",
            "ouder_set-__prefix__-persoon": self.persoon.id,
            "ouder_set-__prefix__-burgerservicenummer_ouder": "",
            "ouder_set-__prefix__-voornamen_ouder": "",
            "ouder_set-__prefix__-geslachtsnaam_ouder": "",
            "ouder_set-__prefix__-geboortedatum_ouder": "",
            "_save": "Opslaan",
        }

        response = self.client.post(self.url, data=test_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Kind.objects.filter(
                burgerservicenummer_kind=kind_burgerservicenummer
            ).exists()
        )
        self.assertTrue(
            Persoon.objects.filter(
                burgerservicenummer_persoon=kind_burgerservicenummer
            ).exists()
        )
        self.assertTrue(
            Ouder.objects.filter(
                burgerservicenummer_ouder=self.persoon.burgerservicenummer_persoon
            ).exists()
        )

    def test_adding_ouder(self):
        ouder_burgerservicenummer = 987654321
        ouder_voornamen = "ouder_voornamen"
        ouder_geslachtsnaam = "ouder_geslachtsnaam"
        ouder_geboortedatum = 20101123

        test_data = {
            "burgerservicenummer_persoon": self.persoon.burgerservicenummer_persoon,
            "voornamen_persoon": self.persoon.voornamen_persoon,
            "geslachtsnaam_persoon": self.persoon.geslachtsnaam_persoon,
            "geboortedatum_persoon": self.persoon.geboortedatum_persoon,
            "geslachtsaanduiding": self.persoon.geslachtsaanduiding,
            "kind_set-TOTAL_FORMS": "0",
            "kind_set-INITIAL_FORMS": "0",
            "kind_set-MIN_NUM_FORMS": "0",
            "kind_set-MAX_NUM_FORMS": "1000",
            "kind_set-__prefix__-id": "",
            "kind_set-__prefix__-persoon": self.persoon.id,
            "kind_set-__prefix__-burgerservicenummer_kind": "",
            "kind_set-__prefix__-voornamen_kind": "",
            "kind_set-__prefix__-geslachtsnaam_kind": "",
            "kind_set-__prefix__-geboortedatum_kind": "",
            "ouder_set-TOTAL_FORMS": "1",
            "ouder_set-INITIAL_FORMS": "0",
            "ouder_set-MIN_NUM_FORMS": "0",
            "ouder_set-MAX_NUM_FORMS": "1000",
            "ouder_set-0-id": "",
            "ouder_set-0-persoon": self.persoon.id,
            "ouder_set-0-burgerservicenummer_ouder": ouder_burgerservicenummer,
            "ouder_set-0-voornamen_ouder": ouder_voornamen,
            "ouder_set-0-geslachtsnaam_ouder": ouder_geslachtsnaam,
            "ouder_set-0-geboortedatum_ouder": ouder_geboortedatum,
            "ouder_set-__prefix__-id": "",
            "ouder_set-__prefix__-persoon": self.persoon.id,
            "ouder_set-__prefix__-burgerservicenummer_ouder": "",
            "ouder_set-__prefix__-voornamen_ouder": "",
            "ouder_set-__prefix__-geslachtsnaam_ouder": "",
            "ouder_set-__prefix__-geboortedatum_ouder": "",
            "_save": "Opslaan",
        }

        response = self.client.post(self.url, data=test_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Ouder.objects.filter(
                burgerservicenummer_ouder=ouder_burgerservicenummer
            ).exists()
        )
        self.assertTrue(
            Persoon.objects.filter(
                burgerservicenummer_persoon=ouder_burgerservicenummer
            ).exists()
        )
        self.assertTrue(
            Kind.objects.filter(
                burgerservicenummer_kind=self.persoon.burgerservicenummer_persoon
            ).exists()
        )
