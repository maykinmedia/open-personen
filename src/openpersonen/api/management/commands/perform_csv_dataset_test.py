from django.core.management import BaseCommand
from django.db.models import Q
from django.urls import reverse

import requests
from rest_framework.authtoken.models import Token

from openpersonen.accounts.models import User
from openpersonen.api.demo_models import *

user, _ = User.objects.get_or_create(username="test")
token, _ = Token.objects.get_or_create(user=user)


class Command(BaseCommand):
    """
    Run using python src/manage.py perform_csv_dataset_test
    """

    help = "Test APIs using demo data in database.  Note: Must have server running at http://localhost:8000"

    def make_request(self, viewname, viewname_kwargs):

        url = reverse(
            viewname,
            kwargs=viewname_kwargs,
        )

        response = requests.get(
            f"http://localhost:8000{url}",
            headers={"Authorization": f"Token {token}"},
        )

        if response.status_code != 200:
            self.stdout.write(
                self.style.ERROR(
                    f"{url} gave a response code of {response.status_code}.  Expected 200"
                )
            )

    def handle(self, **options):

        print(
            "Note: No output will be given when successful (the call returns a 200 response)"
        )
        print("Testing persoon endpoints (this may take a while)")

        for persoon in Persoon.objects.exclude(burgerservicenummer_persoon=""):

            self.make_request(
                "ingeschrevenpersonen-detail",
                {"burgerservicenummer": persoon.burgerservicenummer_persoon},
            )

            self.make_request(
                "kinderen-list",
                {
                    "ingeschrevenpersonen_burgerservicenummer": persoon.burgerservicenummer_persoon
                },
            )

            self.make_request(
                "ouders-list",
                {
                    "ingeschrevenpersonen_burgerservicenummer": persoon.burgerservicenummer_persoon
                },
            )

            self.make_request(
                "partners-list",
                {
                    "ingeschrevenpersonen_burgerservicenummer": persoon.burgerservicenummer_persoon
                },
            )

        print("Testing Partnerschap endpoints")

        for partnerschap in Partnerschap.objects.exclude(
            Q(
                burgerservicenummer_echtgenoot_geregistreerd_partner="",
                persoon__isnull=False,
            )
        ):

            self.make_request(
                "partners-detail",
                {
                    "ingeschrevenpersonen_burgerservicenummer": partnerschap.persoon.burgerservicenummer_persoon,
                    "id": partnerschap.burgerservicenummer_echtgenoot_geregistreerd_partner,
                },
            )

        print("Testing Kind endpoints")

        for kind in Kind.objects.exclude(
            Q(burgerservicenummer_kind="", persoon__isnull=False)
        ):

            self.make_request(
                "kinderen-detail",
                {
                    "ingeschrevenpersonen_burgerservicenummer": kind.persoon.burgerservicenummer_persoon,
                    "id": kind.burgerservicenummer_kind,
                },
            )

        print("Testing Ouder endpoints")

        for ouder in Ouder.objects.exclude(
            Q(burgerservicenummer_ouder="", persoon__isnull=False)
        ):

            self.make_request(
                "ouders-detail",
                {
                    "ingeschrevenpersonen_burgerservicenummer": ouder.persoon.burgerservicenummer_persoon,
                    "id": ouder.burgerservicenummer_ouder,
                },
            )

        print("Done Testing!")
