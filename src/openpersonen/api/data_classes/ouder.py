from dataclasses import dataclass

from django.conf import settings

import xmltodict

from openpersonen.api.demo_models import Persoon as PersoonDemoModel
from openpersonen.api.enum import GeslachtsaanduidingChoices, OuderAanduiding
from openpersonen.api.models import StufBGClient

from .converters.ouder import (
    convert_client_response_to_instance_dict,
    convert_model_instance_to_instance_dict,
)
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
                instance_dict = convert_model_instance_to_instance_dict(instance)
                class_instances.append(cls(**instance_dict))
        else:
            response = StufBGClient.get_solo().get_ouder(bsn)
            result = convert_client_response_to_instance_dict(response)
            if isinstance(result, list):
                class_instances = [cls(**instance_dict) for instance_dict in result]
            else:
                class_instances = [cls(**result)]
        return class_instances

    @classmethod
    def retrieve(cls, bsn, id):
        if getattr(settings, "USE_STUF_BG_DATABASE", False):
            instance = PersoonDemoModel.objects.get(
                burgerservicenummer_persoon=bsn
            ).ouder_set.get(burgerservicenummer_ouder=id)
            result = convert_model_instance_to_instance_dict(instance)
        else:
            response = StufBGClient.get_solo().get_ouder(bsn)
            result = convert_client_response_to_instance_dict(response, id)
        if result:
            if isinstance(result, list) and len(result) == 1:
                result = result[0]
            return cls(**result)
        else:
            return dict()
