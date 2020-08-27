import requests_mock
from django.conf import settings
from django.template import loader
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from openpersonen.accounts.models import User
from openpersonen.api.tests.test_data import partner_retrieve_data


class TestPartner(APITestCase):

    def test_partner_without_token(self):
        response = self.client.get(reverse('partners-list',
                                           kwargs={
                                               'ingeschrevenpersonen_burgerservicenummer': 000000000
                                           }))
        self.assertEqual(response.status_code, 401)

    def test_partner_with_token(self):
        user = User.objects.create(username='test')
        token = Token.objects.create(user=user)
        response = self.client.get(reverse('partners-list',
                                           kwargs={
                                               'ingeschrevenpersonen_burgerservicenummer': 000000000
                                           }), HTTP_AUTHORIZATION=f'Token {token.key}')
        self.assertEqual(response.status_code, 200)

    @requests_mock.Mocker()
    def test_retrieve_partner(self, post_mock):
        post_mock.post(
            settings.STUF_BG_URL,
            content=bytes(loader.render_to_string('ResponsePartner.xml'),
                          encoding='utf-8')
        )

        user = User.objects.create(username='test')
        token = Token.objects.create(user=user)
        response = self.client.get(reverse('partners-list',
                                           kwargs={
                                               'ingeschrevenpersonen_burgerservicenummer': 000000000
                                           }) + '/1',
                                   HTTP_AUTHORIZATION=f'Token {token.key}')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(post_mock.called)
        self.assertEqual(response.json(), partner_retrieve_data)
