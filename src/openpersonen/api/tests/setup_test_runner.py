from django.test.runner import DiscoverRunner

from openpersonen.api.models import StufBGClient


class TestRunner(DiscoverRunner):

    def setup_test_environment(self, **kwargs):
        super(TestRunner, self).setup_test_environment(**kwargs)

        client = StufBGClient.get_solo()
        client.url = "http://fake.test.url"
        client.save()
