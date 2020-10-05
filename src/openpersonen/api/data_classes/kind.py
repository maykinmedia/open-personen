from dataclasses import dataclass

from django.conf import settings

from openpersonen.contrib.demo.models import Persoon as PersoonDemoModel
from openpersonen.contrib.stufbg.models import StufBGClient

from .converters.kind import (
    convert_client_response,
    convert_model_instance_to_instance_dict,
)
from .in_onderzoek import KindInOnderzoek
from .persoon import Persoon


# backend = import_string(settings.OPENPERSONEN_BACKEND)


@dataclass
class Kind(Persoon):
    leeftijd: int
    inOnderzoek: KindInOnderzoek

    @classmethod
    def list(cls, bsn):
        class_instances = []
        if getattr(settings, "OPENPERSONEN_USE_LOCAL_DATABASE", False):
            instances = PersoonDemoModel.objects.get(
                burgerservicenummer_persoon=bsn
            ).kind_set.all()
            for instance in instances:
                instance_dict = convert_model_instance_to_instance_dict(instance)
                class_instances.append(cls(**instance_dict))
        else:
            response = StufBGClient.get_solo().get_kind(bsn)
            result = convert_client_response(response)
            if isinstance(result, dict):
                result = [result]
            class_instances = [cls(**instance_dict) for instance_dict in result]
        return class_instances

    @classmethod
    def retrieve(cls, bsn, id):
        if getattr(settings, "OPENPERSONEN_USE_LOCAL_DATABASE", False):
            instance = PersoonDemoModel.objects.get(
                burgerservicenummer_persoon=bsn
            ).kind_set.get(burgerservicenummer_kind=id)
            result = convert_model_instance_to_instance_dict(instance)
        else:
            response = StufBGClient.get_solo().get_kind(bsn)
            result = convert_client_response(response, id)

            if not result:
                return dict()

            if isinstance(result, list) and len(result) > 0:
                result = result[0]

        return cls(**result)
