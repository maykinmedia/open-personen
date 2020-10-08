from rest_framework.test import APITestCase


class TestAPIRootView(APITestCase):

    def test_api_root(self):
        response = self.client.get('/api', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'{"ingeschrevenpersonen":"http://testserver/api/ingeschrevenpersonen"}', response.content)
