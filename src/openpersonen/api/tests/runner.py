import os

from django.conf import settings
from django.test.runner import DiscoverRunner as _DiscoverRunner

from openpersonen.contrib.stufbg.models import StufBGClient


class DiscoverRunner(_DiscoverRunner):
    def setup_databases(self, **kwargs):
        result = super(DiscoverRunner, self).setup_databases(**kwargs)

        settings.MEDIA_ROOT = os.path.join(
            settings.BASE_DIR, "src/openpersonen/api/tests/media"
        )

        # Ensure correct configuration for unit tests
        client = StufBGClient.get_solo()
        client.url = "http://fake.test.url"
        client.certificate.name = "media/certificate/fake.cert"
        client.certificate_key.name = "media/certificate/fake.key"
        client.ontvanger_applicatie = "Ontvanger applicatie"
        client.zender_applicatie = "Zender applicatie"
        client.save()

        return result
