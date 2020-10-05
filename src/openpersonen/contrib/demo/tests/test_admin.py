from django.urls import reverse

from django_webtest import WebTest
from webtest import Text

from openpersonen.contrib.demo.models import Kind, Ouder, Persoon
from openpersonen.api.tests.factory_models import PersoonFactory, UserFactory


class TestPersoonAdmin(WebTest):
    def setUp(self):
        super().setUp()
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
        self.user = UserFactory(is_superuser=True, is_staff=True, is_active=True)
        self.app.set_user(self.user)

    def test_adding_kind(self):
        kind_burgerservicenummer = 987654321

        response = self.app.get(self.url)

        form = response.forms["persoon_form"]

        form["kind_set-TOTAL_FORMS"] = 1
        form["kind_set-INITIAL_FORMS"] = 0
        form["kind_set-MIN_NUM_FORMS"] = 0
        form["kind_set-MAX_NUM_FORMS"] = 1000
        form["burgerservicenummer_persoon"] = self.persoon.burgerservicenummer_persoon
        form["voornamen_persoon"] = self.persoon.voornamen_persoon
        form["geslachtsnaam_persoon"] = self.persoon.geslachtsnaam_persoon
        form["geboortedatum_persoon"] = self.persoon.geboortedatum_persoon
        form["geslachtsaanduiding"] = self.persoon.geslachtsaanduiding

        text = Text(
            form,
            "input",
            "kind_set-0-persoon",
            1,
            value=self.persoon.id,
            id="kind_set-0-persoon",
        )
        form.field_order.append(("kind_set-0-persoon", text))
        form.fields["kind_set-0-persoon"] = text

        text = Text(
            form,
            "input",
            "kind_set-0-burgerservicenummer_kind",
            1,
            value=kind_burgerservicenummer,
            id="kind_set-0-burgerservicenummer_kind",
        )
        form.field_order.append(("kind_set-0-burgerservicenummer_kind", text))
        form.fields["kind_set-0-burgerservicenummer_kind"] = text

        response = form.submit()

        self.assertTrue(response.status_code, 200)
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

        response = self.app.get(self.url)

        form = response.forms["persoon_form"]

        form["ouder_set-TOTAL_FORMS"] = 1
        form["ouder_set-INITIAL_FORMS"] = 0
        form["ouder_set-MIN_NUM_FORMS"] = 0
        form["ouder_set-MAX_NUM_FORMS"] = 1000
        form["burgerservicenummer_persoon"] = self.persoon.burgerservicenummer_persoon
        form["voornamen_persoon"] = self.persoon.voornamen_persoon
        form["geslachtsnaam_persoon"] = self.persoon.geslachtsnaam_persoon
        form["geboortedatum_persoon"] = self.persoon.geboortedatum_persoon
        form["geslachtsaanduiding"] = self.persoon.geslachtsaanduiding

        text = Text(
            form,
            "input",
            "ouder_set-0-persoon",
            1,
            value=self.persoon.id,
            id="ouder_set-0-persoon",
        )
        form.field_order.append(("ouder_set-0-persoon", text))
        form.fields["ouder_set-0-persoon"] = text

        text = Text(
            form,
            "input",
            "ouder_set-0-burgerservicenummer_ouder",
            1,
            value=ouder_burgerservicenummer,
            id="ouder_set-0-burgerservicenummer_ouder",
        )
        form.field_order.append(("ouder_set-0-burgerservicenummer_ouder", text))
        form.fields["ouder_set-0-burgerservicenummer_ouder"] = text

        response = form.submit()

        self.assertTrue(response.status_code, 200)
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
