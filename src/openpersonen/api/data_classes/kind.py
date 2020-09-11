from dataclasses import dataclass

from django.conf import settings

from openpersonen.api.demo_models import Persoon as PersoonDemoModel
from openpersonen.api.models import StufBGClient

from .converters.kind import (
    convert_client_response_to_instance_dict,
    convert_model_instance_to_instance_dict,
)
from .in_onderzoek import KindInOnderzoek
from .persoon import Persoon


@dataclass
class Kind(Persoon):
    leeftijd: int
    inOnderzoek: KindInOnderzoek

    @classmethod
    def list(cls, bsn):
        class_instances = []
        if getattr(settings, "USE_STUF_BG_DATABASE", False):
            instances = PersoonDemoModel.objects.get(
                burgerservicenummer_persoon=bsn
            ).kind_set.all()
            for instance in instances:
                instance_dict = convert_model_instance_to_instance_dict(instance)
                class_instances.append(cls(**instance_dict))
        return class_instances

    @classmethod
    def retrieve(cls, bsn, id):
        if getattr(settings, "USE_STUF_BG_DATABASE", False):
            instance = PersoonDemoModel.objects.get(
                burgerservicenummer_persoon=bsn
            ).kind_set.get(burgerservicenummer_kind=id)
            instance_dict = convert_model_instance_to_instance_dict(instance)
        else:
            response = StufBGClient.get_solo().get_kind(bsn)
            instance_dict = convert_client_response_to_instance_dict(response)
        return cls(**instance_dict)
