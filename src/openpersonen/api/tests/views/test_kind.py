import requests_mock
from django.conf import settings
from django.template import loader
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from openpersonen.api.tests.test_data import kind_retrieve_data
from openpersonen.accounts.models import User


class TestKind(APITestCase):

    def test_kind_without_token(self):
        response = self.client.get(reverse('kinderen-list',
                                           kwargs={
                                               'ingeschrevenpersonen_burgerservicenummer': 000000000
                                           }))
        self.assertEqual(response.status_code, 401)

    def test_kind_with_token(self):
        user = User.objects.create(username='test')
        token = Token.objects.create(user=user)
        response = self.client.get(reverse('kinderen-list',
                                           kwargs={
                                               'ingeschrevenpersonen_burgerservicenummer': 000000000
                                           }),
                                   HTTP_AUTHORIZATION=f'Token {token.key}')
        self.assertEqual(response.status_code, 200)

    @requests_mock.Mocker()
    def test_detail_kind(self, post_mock):
        post_mock.post(
            settings.STUF_BG_URL,
            content=bytes(loader.render_to_string('ResponseKind.xml'),
                          encoding='utf-8')
        )

        user = User.objects.create(username='test')
        token = Token.objects.create(user=user)
        response = self.client.get(reverse('kinderen-detail',
                                           kwargs={
                                               'ingeschrevenpersonen_burgerservicenummer': 000000000,
                                               'id': 1
                                           }),
                                   HTTP_AUTHORIZATION=f'Token {token.key}')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), kind_retrieve_data)
