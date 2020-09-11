from dataclasses import dataclass
from typing import Optional

from django.conf import settings

from openpersonen.api.demo_models import Persoon as PersoonDemoModel
from openpersonen.api.enum import GeslachtsaanduidingChoices
from openpersonen.api.models import StufBGClient

from .converters.ingeschreven_persoon import (
    convert_client_response_to_instance_dict,
    convert_model_instance_to_instance_dict,
)
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
        if getattr(settings, "USE_STUF_BG_DATABASE", False):
            class_instances = []
            cls.update_filters_to_fit_model(filters)
            instances = PersoonDemoModel.objects.filter(**filters)
            for instance in instances:
                instance_dict = convert_model_instance_to_instance_dict(instance)
                class_instances.append(cls(**instance_dict))
            return class_instances
        else:
            response = StufBGClient.get_solo().get_ingeschreven_persoon(filters=filters)
            instance_dict = convert_client_response_to_instance_dict(response)
            return [cls(**instance_dict)]

    @classmethod
    def retrieve(cls, bsn=None):
        if getattr(settings, "USE_STUF_BG_DATABASE", False):
            instance = PersoonDemoModel.objects.get(burgerservicenummer_persoon=bsn)
            instance_dict = convert_model_instance_to_instance_dict(instance)
        else:
            response = StufBGClient.get_solo().get_ingeschreven_persoon(bsn=bsn)
            instance_dict = convert_client_response_to_instance_dict(response)
        return cls(**instance_dict)
