from dataclasses import dataclass

from openpersonen.backends import backend

from .verblijfs_titel import VerblijfsTitel


@dataclass
class VerblijfsTitelHistorie(VerblijfsTitel):
    geheimhoudingPersoonsgegevens: bool

    @classmethod
    def list(cls, bsn, filters):
        instance_dict = backend.get_verblijfs_titel_historie(bsn, filters)
        return [cls(**instance_dict)]
