from dataclasses import dataclass
from typing import Optional

from openpersonen.api.enum import GeslachtsaanduidingChoices
from openpersonen.backends import backend

from .datum import Datum
from .gezags_verhouding import GezagsVerhouding
from .in_onderzoek import IngeschrevenPersoonInOnderzoek
from .kiesrecht import Kiesrecht
from .naam import IngeschrevenPersoonNaam
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
    kiesrecht: Optional[Kiesrecht]
    inOnderzoek: IngeschrevenPersoonInOnderzoek
    nationaliteit: Nationaliteit
    opschortingBijhouding: OpschortingBijhouding
    overlijden: Optional[Overlijden]
    verblijfplaats: Optional[VerblijfPlaats]
    gezagsverhouding: Optional[GezagsVerhouding]
    verblijfstitel: Optional[VerblijfsTitel]
    reisdocumenten: list

    def get_geslachtsaanduiding_display(self):
        return GeslachtsaanduidingChoices.values[self.geslachtsaanduiding]

    @staticmethod
    def update_filters_to_fit_model(filters):
        query_param_to_model_field_mapping = {
            "geboorte__datum": "geboortedatum_persoon",
            "verblijfplaats__gemeentevaninschrijving": "verblijfplaats__gemeente_van_inschrijving",
            "naam__geslachtsnaam": "geslachtsnaam_persoon",
            "burgerservicenummer": "burgerservicenummer_persoon",
            "verblijfplaats__naamopenbareruimte": "verblijfplaats__naam_openbare_ruimte",
            "verblijfplaats__identificatiecodenummeraanduiding": "verblijfplaats__identificatiecode_nummeraanduiding",
        }

        for (
            query_param_key,
            model_field_key,
        ) in query_param_to_model_field_mapping.items():
            if query_param_key in filters:
                filters[model_field_key] = filters.pop(query_param_key)

    @classmethod
    def list(cls, filters):
        class_instances = []
        instance_dicts = backend.get_person(filters=filters)
        for instance_dict in instance_dicts:
            class_instances.append(cls(**instance_dict))
        return class_instances

    @classmethod
    def retrieve(cls, bsn):
        instance_dicts = backend.get_person(bsn=bsn)
        return cls(**instance_dicts[0])
