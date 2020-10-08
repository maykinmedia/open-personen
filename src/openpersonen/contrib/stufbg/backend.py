from django.apps import apps

from openpersonen.contrib.base import BaseBackend
from openpersonen.contrib.stufbg.converters import *


class BackEnd(BaseBackend):
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

    def get_partner_historie(self, bsn, filters):
        StufBGClient = apps.get_model("stufbg", "StufBGClient")
        response = StufBGClient.get_solo().get_partner_historie(bsn, filters)
        return convert_response_to_partner_historie_dict(response)

    def get_nationaliteit_historie(self, bsn, filters):
        StufBGClient = apps.get_model("stufbg", "StufBGClient")
        response = StufBGClient.get_solo().get_nationaliteit_historie(bsn, filters)
        return convert_response_to_nationaliteit_historie_dict(response)

    def get_verblijf_plaats_historie(self, bsn, filters):
        StufBGClient = apps.get_model("stufbg", "StufBGClient")
        response = StufBGClient.get_solo().get_verblijf_plaats_historie(bsn, filters)
        return convert_response_to_verblijf_plaats_historie_dict(response)

    def get_verblijfs_titel_historie(self, bsn, filters):
        StufBGClient = apps.get_model("stufbg", "StufBGClient")
        response = StufBGClient.get_solo().get_verblijfs_titel_historie(bsn, filters)
        return convert_response_to_verblijfs_titel_historie_dict(response)


default = BackEnd()
