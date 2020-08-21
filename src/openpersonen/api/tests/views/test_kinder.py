from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from openpersonen.accounts.models import User


class TestKinder(APITestCase):

    def test_kinder_without_token(self):
        response = self.client.get(reverse('kinderen-list',
                                           kwargs={
                                               'ingeschrevenpersonen_burgerservicenummer': 000000000
                                           }))
        self.assertEqual(response.status_code, 401)

    def test_kinder_with_token(self):
        user = User.objects.create(username='test')
        token = Token.objects.create(user=user)
        response = self.client.get(reverse('kinderen-list',
                                           kwargs={
                                               'ingeschrevenpersonen_burgerservicenummer': 000000000
                                           }),
                                   HTTP_AUTHORIZATION=f'Token {token.key}')
        self.assertEqual(response.status_code, 200)
