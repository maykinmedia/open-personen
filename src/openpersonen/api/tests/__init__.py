from openpersonen.api.models import StufBGClient

# Set up fake url that fits proper url format
client = StufBGClient.get_solo()
client.url = "http://fake.test.url"
client.save()
