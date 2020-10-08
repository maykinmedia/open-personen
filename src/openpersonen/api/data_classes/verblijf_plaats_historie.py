from dataclasses import dataclass

from openpersonen.backends import backend

from .datum import Datum
from .verblijf_plaats import VerblijfPlaats


@dataclass
class VerblijfPlaatsHistorie(VerblijfPlaats):
    datumTot: Datum
    geheimhoudingPersoonsgegevens: bool

    @classmethod
    def list(cls, bsn, filters):
        instance_dict = backend.get_verblijf_plaats_historie(bsn, filters)
        return [cls(**instance_dict)]
