from dataclasses import dataclass

from openpersonen.backends import backend

from .geboorte import Geboorte
from .naam import Naam


@dataclass
class Persoon:
    burgerservicenummer: str
    geheimhoudingPersoonsgegevens: bool
    naam: Naam
    geboorte: Geboorte

    backend_function_name = None

    @classmethod
    def list(cls, bsn):
        class_instances = []
        function = getattr(backend, cls.backend_function_name)

        if not function:
            raise ValueError(f"No function found with name {cls.backend_function_name}")

        instance_dicts = function(bsn)
        for instance_dict in instance_dicts:
            class_instances.append(cls(**instance_dict))
        return class_instances

    @classmethod
    def retrieve(cls, bsn, id):
        function = getattr(backend, cls.backend_function_name)

        if not function:
            raise ValueError(f"No function found with name {cls.backend_function_name}")

        instance_dicts = function(bsn, id=id)
        return cls(**instance_dicts[0])
