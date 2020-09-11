from dataclasses import dataclass

from django.conf import settings

import xmltodict

from openpersonen.api.demo_models import Persoon as PersoonDemoModel
from openpersonen.api.enum import GeslachtsaanduidingChoices, OuderAanduiding
from openpersonen.api.models import StufBGClient

from .converters.ouder import get_client_instance_dict, get_model_instance_dict
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
        if getattr(settings, "USE_STUF_BG_DATABASE", False):
            instances = PersoonDemoModel.objects.get(
                burgerservicenummer_persoon=bsn
            ).ouder_set.all()
            for instance in instances:
                instance_dict = get_model_instance_dict(instance)
                class_instances.append(cls(**instance_dict))
        return class_instances

    @classmethod
    def retrieve(cls, bsn, id):
        if getattr(settings, "USE_STUF_BG_DATABASE", False):
            instance = PersoonDemoModel.objects.get(
                burgerservicenummer_persoon=bsn
            ).ouder_set.get(burgerservicenummer_ouder=id)
            instance_dict = get_model_instance_dict(instance)
        else:
            response = StufBGClient.get_solo().get_ouder(bsn)
            instance_dict = get_client_instance_dict(response)
        return cls(**instance_dict)
