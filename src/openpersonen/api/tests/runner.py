from django.test.runner import DiscoverRunner as _DiscoverRunner

from openpersonen.api.models import StufBGClient


class DiscoverRunner(_DiscoverRunner):

    def setup_databases(self, **kwargs):
        result = super(DiscoverRunner, self).setup_databases(**kwargs)

        # Ensure correct configuration for unit tests
        client = StufBGClient.get_solo()
        client.url = "http://fake.test.url"
        client.save()

        return result
