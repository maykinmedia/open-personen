from django.core.management import BaseCommand
from django.db.models import Q
from django.urls import reverse

import requests
from rest_framework.authtoken.models import Token

from openpersonen.accounts.models import User
from openpersonen.api.demo_models import *


class Command(BaseCommand):
    """
    Run using python src/manage.py test_csv_dataset
    """

    help = "Test APIs using demo data in database"

    def handle(self, **options):

        user, _ = User.objects.get_or_create(username="test")
        token, _ = Token.objects.get_or_create(user=user)

        print("Note: No output will be given when successful (the call returns a 200 response)")
        print("Beginning testing persoon endpoints (this may take a while)")

        for persoon in Persoon.objects.exclude(burgerservicenummer_persoon=""):

            url = reverse(
                "ingeschrevenpersonen-detail",
                kwargs={"burgerservicenummer": persoon.burgerservicenummer_persoon},
            )

            response = requests.get(
                f"http://localhost:8000{url}",
                headers={"Authorization": f"Token {token}"},
            )

            if response.status_code != 200:
                print(
                    f"{url} gave a response code of {response.status_code}.  Expected 200"
                )

            url = reverse(
                "kinderen-list",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": persoon.burgerservicenummer_persoon
                },
            )

            response = requests.get(
                f"http://localhost:8000{url}",
                headers={"Authorization": f"Token {token}"},
            )

            if response.status_code != 200:
                print(
                    f"{url} gave a response code of {response.status_code}.  Expected 200"
                )

            url = reverse(
                "ouders-list",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": persoon.burgerservicenummer_persoon
                },
            )

            response = requests.get(
                f"http://localhost:8000{url}",
                headers={"Authorization": f"Token {token}"},
            )

            if response.status_code != 200:
                print(
                    f"{url} gave a response code of {response.status_code}.  Expected 200"
                )

            url = reverse(
                "partners-list",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": persoon.burgerservicenummer_persoon
                },
            )

            response = requests.get(
                f"http://localhost:8000{url}",
                headers={"Authorization": f"Token {token}"},
            )

            if response.status_code != 200:
                print(
                    f"{url} gave a response code of {response.status_code}.  Expected 200"
                )

        print("Testing Partnerschap endpoints")

        for partnerschap in Partnerschap.objects.exclude(
            Q(
                burgerservicenummer_echtgenoot_geregistreerd_partner="",
                persoon__isnull=False,
            )
        ):

            url = reverse(
                "partners-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": partnerschap.persoon.burgerservicenummer_persoon,
                    "id": partnerschap.burgerservicenummer_echtgenoot_geregistreerd_partner,
                },
            )

            response = requests.get(
                f"http://localhost:8000{url}",
                headers={"Authorization": f"Token {token}"},
            )

            if response.status_code != 200:
                print(
                    f"{url} gave a response code of {response.status_code}.  Expected 200"
                )

        print("Testing Kind endpoints")

        for kind in Kind.objects.exclude(
            Q(burgerservicenummer_kind="", persoon__isnull=False)
        ):

            url = reverse(
                "kinderen-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": kind.persoon.burgerservicenummer_persoon,
                    "id": kind.burgerservicenummer_kind,
                },
            )

            response = requests.get(
                f"http://localhost:8000{url}",
                headers={"Authorization": f"Token {token}"},
            )

            if response.status_code != 200:
                print(
                    f"{url} gave a response code of {response.status_code}.  Expected 200"
                )

        print("Testing Ouder endpoints")

        for ouder in Ouder.objects.exclude(
            Q(burgerservicenummer_ouder="", persoon__isnull=False)
        ):

            url = reverse(
                "ouders-detail",
                kwargs={
                    "ingeschrevenpersonen_burgerservicenummer": ouder.persoon.burgerservicenummer_persoon,
                    "id": ouder.burgerservicenummer_ouder,
                },
            )

            response = requests.get(
                f"http://localhost:8000{url}",
                headers={"Authorization": f"Token {token}"},
            )

            if response.status_code != 200:
                print(
                    f"{url} gave a response code of {response.status_code}.  Expected 200"
                )

        print("Done Testing!")
