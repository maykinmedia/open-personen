from dataclasses import dataclass

from django.conf import settings
from django.utils.module_loading import import_string

from .in_onderzoek import KindInOnderzoek
from .persoon import Persoon

backend = import_string(settings.OPENPERSONEN_BACKEND)


@dataclass
class Kind(Persoon):
    leeftijd: int
    inOnderzoek: KindInOnderzoek

    @classmethod
    def list(cls, bsn):
        class_instances = []
        instance_dicts = backend.get_kind(bsn)
        for instance_dict in instance_dicts:
            class_instances.append(cls(**instance_dict))
        return class_instances

    @classmethod
    def retrieve(cls, bsn, id):
        instance_dicts = backend.get_kind(bsn, kind_bsn=id)
        return cls(**instance_dicts[0])
