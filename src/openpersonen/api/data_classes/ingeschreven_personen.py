from dataclasses import dataclass

from openpersonen.api.client import client
from openpersonen.api.enum import GeslachtsaanduidingChoices
from openpersonen.api.xml_to_dict_converters import get_ingeschreven_persoon_dict
from .naam import IngeschrevenPersoonNaam
from .datum import Datum
from .gezags_verhouding import GezagsVerhouding
from .in_onderzoek import IngeschrevenPersoonInOnderzoek
from .kiesrecht import Kiesrecht
from .nationaliteit import Nationaliteit
from .opschorting_bijhouding import OpschortingBijhouding
from .overlijden import Overlijden
from .persoon import Persoon
from .verblijf_plaats import VerblijfPlaats
from .verblijfs_titel import VerblijfsTitel


@dataclass
class IngeschrevenPersoon(Persoon):
    naam: IngeschrevenPersoonNaam
    geslachtsaanduiding: str
    leeftijd: int
    datumEersteInschrijvingGBA: Datum
    kiesrecht: Kiesrecht
    inOnderzoek: IngeschrevenPersoonInOnderzoek
    nationaliteit: Nationaliteit
    opschortingBijhouding: OpschortingBijhouding
    overlijden: Overlijden
    verblijfplaats: VerblijfPlaats
    gezagsverhouding: GezagsVerhouding
    verblijfstitel: VerblijfsTitel
    reisdocumenten: list

    def get_geslachtsaanduiding_display(self):
        return GeslachtsaanduidingChoices.values[self.geslachtsaanduiding]

    @classmethod
    def retrieve(cls, bsn):
        response = client.get_natuurlijk_persoon(bsn)
        instance_dict = get_ingeschreven_persoon_dict(response)
        return cls(**instance_dict)
