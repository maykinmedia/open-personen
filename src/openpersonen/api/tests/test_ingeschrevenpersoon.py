from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from openpersonen.accounts.models import User


class TestIngeschrevenPersoon(APITestCase):

    def test_ingeschreven_persoon_without_token(self):
        response = self.client.get(reverse('ingeschrevenpersonen-list'))
        self.assertEqual(response.status_code, 401)

    def test_ingeschreven_persoon_with_token(self):
        user = User.objects.create(username='test')
        token = Token.objects.create(user=user)
        response = self.client.get(reverse('ingeschrevenpersonen-list'), HTTP_AUTHORIZATION=f'Token {token.key}')
        self.assertEqual(response.status_code, 200)
