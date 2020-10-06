from dataclasses import dataclass

from django.conf import settings
from django.utils.module_loading import import_string

from openpersonen.api.enum import GeslachtsaanduidingChoices, SoortVerbintenis

from .aangaan_huwelijk_partnerschap import AangaanHuwelijkPartnerschap
from .in_onderzoek import PartnerInOnderzoek
from .persoon import Persoon


@dataclass
class Partner(Persoon):
    geslachtsaanduiding: str
    soortVerbintenis: str
    inOnderzoek: PartnerInOnderzoek
    aangaanHuwelijkPartnerschap: AangaanHuwelijkPartnerschap

    def get_geslachtsaanduiding_display(self):
        return GeslachtsaanduidingChoices.values[self.geslachtsaanduiding]

    def get_soortVerbintenis_display(self):
        return SoortVerbintenis.values[self.soortVerbintenis]

    @classmethod
    def list(cls, bsn):
        class_instances = []
        backend = import_string(settings.OPENPERSONEN_BACKEND)
        instance_dicts = backend.get_partner(bsn)
        for instance_dict in instance_dicts:
            class_instances.append(cls(**instance_dict))
        return class_instances

    @classmethod
    def retrieve(cls, bsn, id):
        backend = import_string(settings.OPENPERSONEN_BACKEND)
        instance_dicts = backend.get_partner(bsn, partner_bsn=id)
        return cls(**instance_dicts[0])
