from rest_framework import serializers

from openpersonen.api.enum import GeslachtsaanduidingChoices

from .datum import DatumSerializer
from .gezags_verhouding import GezagsVerhoudingSerializer
from .in_onderzoek import IngeschrevenPersoonInOnderzoekSerializer
from .kiesrecht import KiesrechtSerializer
from .naam import IngeschrevenPersoonNaamSerializer
from .nationaliteit import NationaliteitSerializer
from .opschorting_bijhouding import OpschortingBijhoudingSerializer
from .overlijden import OverlijdenSerializer
from .persoon import PersoonSerializer
from .verblijf_plaats import VerblijfPlaatsSerializer
from .verblijfs_titel import VerblijfsTitelSerializer


class IngeschrevenPersoonSerializer(PersoonSerializer):
    naam = IngeschrevenPersoonNaamSerializer(required=False)
    geslachtsaanduiding = serializers.ChoiceField(
        choices=GeslachtsaanduidingChoices.choices, required=False
    )
    leeftijd = serializers.IntegerField(max_value=999, required=False)
    datumEersteInschrijvingGBA = DatumSerializer(required=False)
    kiesrecht = KiesrechtSerializer(required=False)
    inOnderzoek = IngeschrevenPersoonInOnderzoekSerializer(required=False)
    nationaliteit = NationaliteitSerializer(many=True, required=False)
    opschortingBijhouding = OpschortingBijhoudingSerializer(required=False)
    overlijden = OverlijdenSerializer(required=False)
    verblijfplaats = VerblijfPlaatsSerializer(required=False)
    gezagsverhouding = GezagsVerhoudingSerializer(required=False)
    verblijfstitel = VerblijfsTitelSerializer(required=False)
    reisdocumenten = serializers.ListField(
        child=serializers.CharField(max_length=9), required=False
    )

    expand_fields = {'kinderen', 'ouders', 'partners'}

    def to_representation(self, instance):
        result = super().to_representation(instance)

        if 'expand' in self.context['request'].GET:
            query_params = set(self.context['request'].GET['expand'].split(','))
            if not query_params.issubset(self.expand_fields):
                raise ValueError("Bad expand query params")

            for param in query_params:
                result[param] = getattr(instance, param)

        return result
