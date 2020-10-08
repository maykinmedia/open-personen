from dataclasses import dataclass

from openpersonen.backends import backend

from .datum import Datum
from .nationaliteit import Nationaliteit
from .waarde import Waarde


@dataclass
class NationaliteitHistorie(Nationaliteit):
    geheimhoudingPersoonsgegevens: bool
    datumEindeGeldigheid: Datum
    redenBeeindigen: Waarde
    indicatieNationaliteitBeeindigd: bool

    @classmethod
    def list(cls, bsn, filters):
        instance_dict = backend.get_nationaliteit_historie(bsn, filters)
        return [cls(**instance_dict)]
