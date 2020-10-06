from django.apps import apps

from openpersonen.contrib.stufbg.converters import *


class BackEnd:
    # Note: All methods must return a list of dicts

    def get_person(self, bsn=None, filters=None):
        if not bsn and not filters:
            raise ValueError("Either bsn or filters must be supplied")

        StufBGClient = apps.get_model("stufbg", "StufBGClient")

        if bsn:
            response = StufBGClient.get_solo().get_ingeschreven_persoon(bsn=bsn)
        else:
            response = StufBGClient.get_solo().get_ingeschreven_persoon(filters=filters)

        return convert_response_to_persoon_dicts(response)

    def get_kind(self, bsn, **kwargs):
        StufBGClient = apps.get_model("stufbg", "StufBGClient")
        return StufBGClient.get_solo().get_kind(bsn)

    def get_ouder(self, bsn, **kwargs):
        StufBGClient = apps.get_model("stufbg", "StufBGClient")
        return StufBGClient.get_solo().get_ouder(bsn)

    def get_partner(self, bsn, **kwargs):
        StufBGClient = apps.get_model("stufbg", "StufBGClient")
        return StufBGClient.get_solo().get_partner(bsn)
