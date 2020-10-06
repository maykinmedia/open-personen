from dataclasses import dataclass

from django.conf import settings
from django.utils.module_loading import import_string

from openpersonen.api.enum import GeslachtsaanduidingChoices, OuderAanduiding

from .datum import Datum
from .in_onderzoek import OuderInOnderzoek
from .persoon import Persoon


@dataclass
class Ouder(Persoon):
    geslachtsaanduiding: str
    ouderAanduiding: str
    datumIngangFamilierechtelijkeBetrekking: Datum
    inOnderzoek: OuderInOnderzoek

    def get_geslachtsaanduiding_display(self):
        return GeslachtsaanduidingChoices.values[self.geslachtsaanduiding]

    def get_ouderAanduiding_display(self):
        return OuderAanduiding.values[self.ouderAanduiding]

    @classmethod
    def list(cls, bsn):
        class_instances = []
        backend = import_string(settings.OPENPERSONEN_BACKEND)
        instance_dicts = backend.get_ouder(bsn)
        for instance_dict in instance_dicts:
            class_instances.append(cls(**instance_dict))
        return class_instances

    @classmethod
    def retrieve(cls, bsn, id):
        backend = import_string(settings.OPENPERSONEN_BACKEND)
        instance_dicts = backend.get_ouder(bsn, ouder_bsn=id)
        return cls(**instance_dicts[0])
