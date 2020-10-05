from dataclasses import dataclass

from django.conf import settings

from openpersonen.api.demo_models import Persoon as PersoonDemoModel
from openpersonen.api.enum import GeslachtsaanduidingChoices, SoortVerbintenis
from openpersonen.api.models import StufBGClient

from .aangaan_huwelijk_partnerschap import AangaanHuwelijkPartnerschap
from .converters.partner import (
    convert_client_response,
    convert_model_instance_to_instance_dict,
)
from .in_onderzoek import PartnerInOnderzoek
from .persoon import Persoon


@dataclass
class Partner(Persoon):
    geslachtsaanduiding: str
    soortVerbintenis: str
    inOnderzoek: PartnerInOnderzoek
    aangaanHuwelijkPartnerschap: AangaanHuwelijkPartnerschap

    def get_geslachtsaanduiding_display(self):
        return GeslachtsaanduidingChoices.values[self.geslachtsaanduiding]

    def get_soortVerbintenis_display(self):
        return SoortVerbintenis.values[self.soortVerbintenis]

    @classmethod
    def list(cls, bsn):
        class_instances = []
        if getattr(settings, "OPENPERSONEN_USE_LOCAL_DATABASE", False):
            instances = PersoonDemoModel.objects.get(
                burgerservicenummer_persoon=bsn
            ).partnerschap_set.all()
            for instance in instances:
                instance_dict = convert_model_instance_to_instance_dict(instance)
                class_instances.append(cls(**instance_dict))
        else:
            response = StufBGClient.get_solo().get_partner(bsn)
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
            ).partnerschap_set.get(
                burgerservicenummer_echtgenoot_geregistreerd_partner=id
            )
            result = convert_model_instance_to_instance_dict(instance)
        else:
            response = StufBGClient.get_solo().get_partner(bsn)
            result = convert_client_response(response, id)

            if not result:
                return dict()

            if isinstance(result, list) and len(result) > 0:
                result = result[0]

        return cls(**result)
