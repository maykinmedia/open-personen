from django.apps import apps


class BackEnd:
    def get_person(self, bsn=None, filters=None):
        if not bsn and not filters:
            raise ValueError("Either bsn or filters must be supplied")

        StufBGClient = apps.get_model("stufbg", "StufBGClient")

        if bsn:
            return StufBGClient.get_solo().get_ingeschreven_persoon(bsn=bsn)
        else:
            return StufBGClient.get_solo().get_ingeschreven_persoon(filters=filters)

    def get_kind(self, bsn, **kwargs):
        StufBGClient = apps.get_model("stufbg", "StufBGClient")
        return StufBGClient.get_solo().get_kind(bsn)

    def get_ouder(self, bsn, **kwargs):
        StufBGClient = apps.get_model("stufbg", "StufBGClient")
        return StufBGClient.get_solo().get_ouder(bsn)

    def get_partner(self, bsn, **kwargs):
        StufBGClient = apps.get_model("stufbg", "StufBGClient")
        return StufBGClient.get_solo().get_partner(bsn)
