import requests

from rest_framework.authtoken.models import Token

from openpersonen.accounts.models import User

from django.core.management import BaseCommand
from django.urls import reverse

from openpersonen.api.demo_models import *

class Command(BaseCommand):
    """
    Run using python src/manage.py test_csv_dataset
    """

    help = "Test APIs using demo data in database"

    def handle(self, **options):

        user, _ = User.objects.get_or_create(username="test")
        token, _ = Token.objects.get_or_create(user=user)

        print('Beginning testing persoon endpoints')

        for persoon in Persoon.objects.exclude(burgerservicenummer_persoon=''):

            url = reverse(
                    "ingeschrevenpersonen-detail",
                    kwargs={"burgerservicenummer": persoon.burgerservicenummer_persoon},
                )

            response = requests.get(f'http://localhost:8000{url}', headers={'Authorization': f'Token {token}'})

            if response.status_code != 200:
                print(f'{url} gave a response code of {response.status_code}.  Expected 200')
