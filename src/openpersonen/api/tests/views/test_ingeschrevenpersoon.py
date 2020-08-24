import requests_mock
from django.urls import reverse
from django.conf import settings
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

    @requests_mock.Mocker()
    def test_retrieve_ingeschreven_persoon(self, post_mock):

        post_mock.post(
            settings.STUF_BG_URL
        )

        user = User.objects.create(username='test')
        token = Token.objects.create(user=user)
        response = self.client.get(reverse('ingeschrevenpersonen-list') + '/123456789',
                                   HTTP_AUTHORIZATION=f'Token {token.key}')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
