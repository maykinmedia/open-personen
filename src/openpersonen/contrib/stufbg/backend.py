from django.apps import apps

from openpersonen.contrib.base import BaseBackend
from openpersonen.contrib.stufbg.converters import *


class BackEnd(BaseBackend):
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

    def get_kind(self, bsn, id=None):
        StufBGClient = apps.get_model("stufbg", "StufBGClient")
        response = StufBGClient.get_solo().get_kind(bsn)
        return convert_response_to_kind_dict(response, id=id)

    def get_ouder(self, bsn, id=None):
        StufBGClient = apps.get_model("stufbg", "StufBGClient")
        response = StufBGClient.get_solo().get_ouder(bsn)
        return convert_response_to_ouder_dict(response, id=id)

    def get_partner(self, bsn, id=None):
        StufBGClient = apps.get_model("stufbg", "StufBGClient")
        response = StufBGClient.get_solo().get_partner(bsn)
        return convert_response_to_partner_dict(response, id=id)


default = BackEnd()
